from django.contrib import admin

from .models import Events, Sensors


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor_id', 'name', 'temperature', 'humidity')


class SensorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')


admin.site.register(Events, EventsAdmin)
admin.site.register(Sensors, SensorsAdmin)
