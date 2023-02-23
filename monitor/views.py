from django.shortcuts import render, redirect
from django.http import HttpResponse
from monitor.models import SensorProfile, LoggingRecord

def homepage(request):
    context_dict = {}
    return render(request,'monitor_templates/homepage.html', context=context_dict)

def sensor(request):
    context_dict = {}
    return render(request, 'monitor_templates/sensor.html', context=context_dict)

def info(request):
    context_dict = {}
    return render(request, 'monitor_templates/info.html', context=context_dict)  


def registerSensor(request):
    if request.method == 'GET':
        try:
            new_sensor_id = request.GET.get('id')
            if new_sensor_id is None:
                return HttpResponse('ERR02 No-id-Field-Given')
            if SensorProfile.objects.filter(id=new_sensor_id).exists():
                return HttpResponse("ERR03 Sensor-already-registered")
            else:
                new_sensor = SensorProfile(id=new_sensor_id, location="")
                new_sensor.save()
                return HttpResponse('Successful-Registration')
        except KeyError:
            return HttpResponse('ERR02 No-id-Field-Given')
        except Exception as e:
            print(e)
            return HttpResponse('ERR00 Unknown-Error')
    else:
        return HttpResponse('ERR01 Incorrect-Request-Type')


def addRecord(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            time = request.POST.get('time')
            data = request.POST.get('data')
            decision = ""#call NNModel object and pass it the data, then put the result here
            if SensorProfile.objects.filter(sensor=id, time_logged=time).exists():
                raise Exception("ERR13 Sound-Already-Logged")
            else:
                new_record = LoggingRecord(time_logged=time, sound_category=decision, sensor=id)
                new_record.save()
                return HttpResponse('Sound-Logged-Successfully')
        except KeyError:
            return HttpResponse('ERR12 Incorrect-fields-given')
        except Exception as e:
            print(e)
            return HttpResponse('ERR00 Unknown-Error')
    else:
        return HttpResponse('ERR11 Incorrect-Request-Type')

