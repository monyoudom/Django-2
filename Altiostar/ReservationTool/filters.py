import django_filters
from .models import *
#from inventory_app.models import Form1
#import datetime


class ItemFilter(django_filters.FilterSet):
    setup_name = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined__gt = django_filters.NumberFilter(field_name='date', lookup_expr='year__gt')
    # year_joined__lt = django_filters.NumberFilter(field_name='date', lookup_expr='year__lt')
    # date_received__gt = django_filters.DateFilter(field_name='date', lookup_expr='date__gt')
    # date_received__lt = django_filters.DateFilter(field_name='date', lookup_expr='date__lt')
    #date_between = django_filters.DateFromToRangeFilter(field_name='date', label='Date (Between) in format YYYY-MM-DD' )
   # inward = django_filters.CharFilter(lookup_expr=)
    class Meta:
        model = Setup
        fields = ['setup_name']

   # item = django_filters.CharFilter(field_name='item', lookup_expr='icontains')