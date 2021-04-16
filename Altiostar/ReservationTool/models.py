from django.db import models

# Create your models here.
class Device(models.Model):
    hostname = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125,unique=True)
    serial_number  = models.CharField(max_length=125)
    ip = models.CharField(max_length=125)
    mac = models.CharField(max_length=125)
    device_type = models.CharField(max_length=125)
    make = models.CharField(max_length=125)


    def __str__(self):
      return self.device_type

class Setup(models.Model):
    setup_name = models.CharField(max_length=125)
    device_type = models.ForeignKey(Device, on_delete=models.CASCADE)
   # setup_type = models.CharField(max_length=125)

   # attenuator = models.CharField(max_length=125)


    def __str__(self):
      return self.setup_name