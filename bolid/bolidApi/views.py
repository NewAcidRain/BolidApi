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

def StartPage(request):
    return redirect("/admin/")


class CreateEvents(GenericAPIView):
    serializer_class = EventsCreateSerializer
    queryset = Events.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_create_events)
    def post(self, request):
        serializer = EventsCreateSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class GetEvents(ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'temperature', 'humidity']

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateEvents(GenericAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_update_events)
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
    serializer_class = EventSerializer
    queryset = Events.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_delete_events)
    def delete(self, request, pk):
        try:
            event = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response("Event does not exist", status=404)
        event.delete()
        event.save()
        return Response(f"Event id = {pk} was deleted", status=200)


class CreateSensors(GenericAPIView):
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_create_sensors)
    def post(self, request):
        serializer = SensorsSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid Data")


class GetSensors(ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UpdateSensors(GenericAPIView):
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_update_sensors)
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
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

    @swagger_auto_schema(responses=response_schema_dict_delete_sensors)
    def delete(self, request, pk):
        try:
            event = Sensors.objects.get(pk=pk)
        except Sensors.DoesNotExist:
            return Response("Event does not exist", status=404)
        event.delete()
        event.save()
        return Response(f"Sensor id = {pk} was deleted", status=200)
