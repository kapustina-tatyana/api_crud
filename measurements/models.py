from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True

    )


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
