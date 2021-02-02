from django.db import models


class Sensor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # example --> 28-3c01d607df32
    uuid = models.CharField(max_length=100)

    # example --> DS18B20
    sensor_model = models.CharField(max_length=255)

    # example --> sensor_1
    title = models.CharField(max_length=255)

    # example --> This sensor used in room number 2
    description = models.TextField(max_length=10000)

    # example --> 1 (temperature)
    type = models.ForeignKey(to="metrics.SensorType", on_delete=models.CASCADE)

    # example --> 2 (celsius)
    unit = models.ForeignKey(to="metrics.Unit", on_delete=models.CASCADE)

    def __str__(self):
        return self.uuid


class SensorType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # example --> temperature
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Unit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # example --> celsius
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class   Log(models.Model):
    # example --> 1 (ds18b20)
    sensor = models.ForeignKey(to="metrics.Sensor", on_delete=models.CASCADE)

    created_at_by_server = models.DateTimeField(auto_now_add=True)
    updated_at_by_server = models.DateTimeField(auto_now=True)

    logged_at = models.DateTimeField()

    temp = models.FloatField(verbose_name="temperature", null=True)
    voltage = models.FloatField(null=True)
    current = models.FloatField(null=True)
    resistance = models.FloatField(null=True)
