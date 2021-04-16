import django_filters
from .models import *
#from inventory_app.models import Form1
#import datetime


class SetupFilter(django_filters.FilterSet):
    setup_name = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model = Setup
        fields = ['setup_name']

class DeviceFilter(django_filters.FilterSet):
    hostname = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model = Device  
        fields = ['hostname']
