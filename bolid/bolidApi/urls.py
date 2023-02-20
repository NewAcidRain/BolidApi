from django.urls import path, include

from .views import *

urlpatterns = [
    path('api/create_events', CreateEvents.as_view()),
    path('',StartPage),
    path('api/parse',EventsParse.as_view()),
    path('api/read_events', GetEvents.as_view()),
    path('api/update_event/<int:pk>', UpdateEvents.as_view()),
    path('api/delete_event/<int:pk>', DeleteEvents.as_view()),
    path('api/create_sensors', CreateSensors.as_view()),
    path('api/read_sensors', GetSensors.as_view()),
    path('api/update_sensor/<int:pk>', UpdateSensors.as_view()),
    path('api/delete_sensor/<int:pk>', DeleteSensors.as_view()),

]

