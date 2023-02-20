from rest_framework import serializers

from .models import Events, Sensors


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = "__all__"

    def create(self, validated_data):
        return Sensors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.type = validated_data.get('type')
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensors.objects.all())

    class Meta:
        model = Events
        fields = ['id', 'sensor_id', 'name', 'temperature', 'humidity']

    def create(self, validated_data):
        return Events.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sensor_id = validated_data.get('sensor_id')
        instance.name = validated_data.get('name')
        instance.temperature = validated_data.get('temperature')
        instance.humidity = validated_data.get('humidity')
        instance.save()
        return instance


class EventsCreateSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensors.objects.all())

    class Meta:
        model = Events
        fields = ['id', 'sensor_id', 'name', 'temperature', 'humidity']
