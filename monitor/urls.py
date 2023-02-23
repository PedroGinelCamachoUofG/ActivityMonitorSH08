from django.urls import path
from monitor import views

app_name = 'monitor'

urlpatterns = [
    path ('', views.homepage, name ='homepage'),
    path('sensor/', views.sensor, name = 'sensor'),
    path('info/', views.info, name='info'),
    path('register-sensor/', views.registerSensor, name='register-sensor'),
    path('add-record/', views.addRecord, name='add-record'),
]