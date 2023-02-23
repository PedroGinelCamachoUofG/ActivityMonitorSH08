from django.db import models
import numpy as np
#from ndarraydjango.fields import NDArrayField
#from ndarray import NDArrayField


# UP FOR MASSIVE CHANGES AS WE NEED TO DISCUSS THESE!

class Model(models.Model):
    #vec1 = NDArrayField(shape=(32, 4), dtype=np.float64)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Models'

class SensorProfile(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=4)
    location = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'SensorProfiles'

class LoggingRecord(models.Model):
    time_logged = models.TimeField()
    sound_category = models.CharField(max_length=30)
    sensor = models.ForeignKey(SensorProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'LoggingRecords'
