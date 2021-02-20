from rest_framework import serializers
from .models import *


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ['id', 'name']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class SensorListSerializer(serializers.ModelSerializer):
    """ GET --> just a list of all sensors"""

    class Meta:
        model = Sensor
        fields = [
            # read_only_fields
            'sensor_model',
            'id',
            'title',
            'description',
            'type',
            'unit',
        ]
        read_only_fields = ['sensor_model',
                            'id',
                            'title',
                            'description',
                            'type',
                            'unit',
                            ]


class SensorDetailSerializer(serializers.ModelSerializer):

    """ just GET the whole information of all sensors """

    type = SensorTypeSerializer()
    unit = UnitSerializer()

    class Meta:
        model = Sensor
        fields = [

            # read_only_fields
            'id',
            'sensor_model',
            'title',
            'description',
            'type',
            'unit',
        ]
        read_only_fields = ['sensor_model',
                            'id',
                            'title',
                            'description',
                            'type',
                            'unit',
                            ]


class LogCreateSerializer(serializers.ModelSerializer):
    """ POST --> just create logs """

    uuid = serializers.CharField(source="sensor.uuid")

    def validate(self, data):
        validated_data = super(LogCreateSerializer, self).validate(data)

        # sensor's uuid must registered with in system
        if not Sensor.objects.filter(uuid=validated_data['sensor']['uuid']).exists():
            raise serializers.ValidationError("This uuid not registered yet")

        return validated_data

    def create(self, validated_data):
        sensor_id = Sensor.objects.get(uuid=validated_data['sensor']['uuid'])
        log_obj = Log(sensor=sensor_id, logged_at=validated_data['logged_at'], temp=validated_data['temp'])
        log_obj.save()

        return log_obj

    class Meta:
        model = Log
        fields = [
            'logged_at',
            'temp',
            'uuid'
        ]


class LogListSerializer(serializers.ModelSerializer):
    """ just return a list of logs """

    sensor = SensorDetailSerializer()

    class Meta:
        model = Log
        fields = ['id',
                  'sensor',
                  'logged_at',
                  'temp',
                  'voltage',
                  'current',
                  'resistance']

        read_only_fields = ['id',
                            'sensor',
                            'logged_at',
                            'temp',
                            'voltage',
                            'current',
                            'resistance']


class LogDetailSerializer(serializers.ModelSerializer):

    sensor = SensorDetailSerializer()

    class Meta:
        model = Log
        fields = [

            # read_only_fields
            'id',
            'sensor',
            'created_at',
            'updated_at',
            'logged_at',
            'temp',
            'voltage',
            'current',
            'resistance']

        read_only_fields = [
            'id',
            'sensor',
            'created_at',
            'updated_at',
            'logged_at',
            'temp',
            'voltage',
            'current',
            'resistance']


