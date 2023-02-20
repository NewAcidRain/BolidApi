from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from .models import Events, Sensors
from .serializers import EventSerializer, SensorsSerializer, EventsCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from .responses import *
from rest_framework.parsers import FileUploadParser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated


def StartPage(request):
    return redirect("/admin/")


class CreateEvents(GenericAPIView):
    serializer_class = EventsCreateSerializer
    queryset = Events.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses=response_schema_dict_create_events,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def post(self, request):
        serializer = EventsCreateSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class GetEvents(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'temperature', 'humidity']

    @swagger_auto_schema(responses=response_schema_dict_delete_sensors,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateEvents(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Events.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_update_events,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def post(self, request, pk):
        if not pk:
            return Response("Method POST is not allowed", status=400)
        try:
            instance = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response("Event does not exist", status=404)
        serializer = EventSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class DeleteEvents(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Events.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_delete_events,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def delete(self, request, pk):
        try:
            event = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response("Event does not exist", status=404)
        event.delete()
        event.save()
        return Response(f"Event id = {pk} was deleted", status=200)


class CreateSensors(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_create_sensors,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def post(self, request):
        serializer = SensorsSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid Data")


class GetSensors(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    @swagger_auto_schema(manual_parameters=[openapi.Parameter(
        name="Authorization",
        description="Authorization token",
        required=True,
        type=openapi.TYPE_STRING,
        in_=openapi.IN_HEADER,
    ), ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateSensors(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_update_sensors,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def post(self, request, pk):
        if not pk:
            return Response("Method POST is not allowed", status=400)
        try:
            instance = Sensors.objects.get(pk=pk)
        except Sensors.DoesNotExist:
            return Response("Sensor does not exist", status=404)
        serializer = SensorsSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DeleteSensors(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_delete_sensors,
                         manual_parameters=[openapi.Parameter(
                             name="Authorization",
                             description="Authorization token",
                             required=True,
                             type=openapi.TYPE_STRING,
                             in_=openapi.IN_HEADER,
                         ), ]
                         )
    def delete(self, request, pk):
        try:
            event = Sensors.objects.get(pk=pk)
        except Sensors.DoesNotExist:
            return Response("Event does not exist", status=404)
        event.delete()
        event.save()
        return Response(f"Sensor id = {pk} was deleted", status=200)


class EventsParse(APIView):
    permission_classes = [IsAuthenticated]
    parser_class = FileUploadParser

    @swagger_auto_schema(operation_description="Need to use postman or smth, add .json file", )
    def put(self, request):
        file = request.data
        print(file)
        for i in file:
            try:
                sensor_id = Sensors.objects.get(id=i['sensor_id'])
            except Sensors.ObjectDoesNotExist:
                return Response("Invalid JSON data", status=400)
            name = i['name']
            try:
                temperature = i['temperature']
                humidity = i['humidity']
            except KeyError:
                temperature = None
                humidity = None
            Events.objects.create(sensor_id=sensor_id, name=name, temperature=temperature, humidity=humidity)
        return Response(status=200)
