from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

TYPE_CHOICE = ((1, '1'), (2, '2'), (3, '3'),)


class Events(models.Model):
    sensor_id = models.ForeignKey('Sensors', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    temperature = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


class Sensors(models.Model):
    TYPE_CHOICE = ((1, '1'), (2, '2'), (3, '3'),)
    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE_CHOICE, default=1)

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.name
