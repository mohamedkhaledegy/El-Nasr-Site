from cProfile import label
from django.db.models import fields
import django_filters
from django_filters.filters import CharFilter
from django import forms
from .models import *

class StoreFilter(django_filters.FilterSet):
    #price__gt = django_filters.NumberFilter(field_name='priceDev', lookup_expr='gt')
    class Meta:
        model = Store
        fields = {
            'name':['icontains'], 
            'address_store':['icontains'],
            'city': ['exact'],
            }
        #exclude = ['imageDev','img_dev_full_1','img_dev_full_2']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.BooleanField:{
                'filter_class':django_filters.BooleanFilter,
                'extra':lambda f: {
                    'widget': forms.CheckboxInput
                }
            }
        }

class VisitFilter(django_filters.FilterSet):
    class Meta:
        model = Visit
        fields = '__all__'