from rest_framework import viewsets
from .models import *
from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend


class LogViewSet(viewsets.GenericViewSet,
                 viewsets.mixins.CreateModelMixin,
                 viewsets.mixins.ListModelMixin,
                 viewsets.mixins.RetrieveModelMixin):

    """
        POST:
            "create" --> http://192.168.88.50:8000/api/metrics/logs/
            To create new log
            send me:
                "logged_at": the time of log in this format(2021-01-04 15:27:57)
                "temp": the temperature
                "uuid": the uuid of sensor

        GET:

            "list" --> http://192.168.88.50:8000/api/metrics/log/?limit=2&offset=10&sensor=1

                To receive a list of recent logs
                example result -->
                                {
                                    "id": 135,
                                    "sensor": {
                                        "sensor_model": "ds18b20",
                                        "id": 1,
                                        "title": "sensor_1",
                                        "description": "This sensor used in room number 2",
                                        "type": 1,
                                        "unit": 2
                                    },
                                    "logged_at": "2021-01-04T15:58:53.645127Z",
                                    "temp": 24.875,
                                    "voltage": null,
                                    "current": null,
                                    "resistance": null
                                },


            "retrieve" -->  http://localhost:8000/api/metrics/log/171/

                retrieve complete details of a log
                example result -->
                                {
                                    "id": 171,
                                    "sensor": {
                                        "id": 1,
                                        "sensor_model": "ds18b20",
                                        "title": "sensor_1",
                                        "description": "This sensor used in room number 2",
                                        "type": {
                                            "id": 1,
                                            "name": "tempurature"
                                        },
                                        "unit": {
                                            "id": 2,
                                            "name": "celsius"
                                        }
                                    },
                                    "created_at": "2021-01-04T12:35:23.457838Z",
                                    "updated_at": "2021-01-04T12:35:23.457859Z",
                                    "logged_at": "2021-01-04T15:58:53.645127Z",
                                    "temp": 24.875,
                                    "voltage": null,
                                    "current": null,
                                    "resistance": null
                                }
    """

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor']

    def get_queryset(self):

        # if self.action == 'create':

        if self.action == 'list':
            return Log.objects.all().order_by('-logged_at')

        if self.action == 'retrieve':
            return Log.objects.all()

    def get_serializer_class(self):

        if self.action == 'create':
            return LogCreateSerializer

        if self.action == 'list':
            return LogListSerializer

        if self.action == 'retrieve':
            return LogDetailSerializer


class SensorsViewSet(viewsets.GenericViewSet,
                     viewsets.mixins.ListModelMixin,
                     viewsets.mixins.RetrieveModelMixin):

    """
        GET:
            "list" -->  http://localhost:8000/api/metrics/sensors/
                        http://localhost:8000/api/metrics/sensors/?type=1
                returns a list of all sensors

                example result -->  {
                                        "count": 2,
                                        "next": null,
                                        "previous": null,
                                        "results": [
                                            {
                                                "sensor_model": "ds18b20",
                                                "id": 1,
                                                "title": "sensor_1",
                                                "description": "This sensor used in room number 2",
                                                "type": 1,
                                                "unit": 2
                                            },
                                            {
                                                "sensor_model": "ds18b20",
                                                "id": 2,
                                                "title": "sensor_2",
                                                "description": "this sensor used in room number 28",
                                                "type": 1,
                                                "unit": 2
                                            }
                                        ]
                                    }

            "retrieve" --> http://localhost:8000/api/metrics/sensors/1

                example result -->  {
                            "sensor_model": "ds18b20",
                            "id": 1,
                            "title": "sensor_1",
                            "description": "This sensor used in room number 2",
                            "type": 1,
                            "unit": 2
                        }

    """

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Sensor.objects.all()

    def get_serializer_class(self):

        if self.action == 'list':
            return SensorListSerializer

        if self.action == 'retrieve':
            return SensorDetailSerializer


class SensorTypeViewSet(viewsets.GenericViewSet,
                        viewsets.mixins.ListModelMixin):
    """
        "GET":
            "list" -- > return a list of types of sensors
                example-result --> {
                            "count": 2,
                            "next": null,
                            "previous": null,
                            "results": [
                                {
                                    "name": "tempurature",
                                    "id": 1
                                },
                                {
                                    "name": "gravity",
                                    "id": 2
                                }
                            ]
                        }
    """

    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer