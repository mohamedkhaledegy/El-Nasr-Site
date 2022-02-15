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
            'user_admin':['exact'],
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


########################################
###################################
################## Faults
########################################
###################################
class FaultFilter(django_filters.FilterSet):
    class Meta:
        model = Fault
        fields = '__all__'
class FaultFilterStaff(django_filters.FilterSet):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at',
        'fixed_at',
        'active',
        'active_tosend',
        'need_to_approve',
        'approved_to_repair',
        ]
class FaultFilterAdmen(django_filters.FilterSet):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at','active',
        'fixed_at','need_to_approve',
        'approved_to_repair',
        ]

class VisitFilterAdmen(django_filters.FilterSet):
    class Meta:
        model = Visit
        fields = {
            'store':['exact'], 
            'short_desc':['icontains'],
            'store__city': ['icontains'],
        }
        
########################################
###################################
################## visits
########################################
###################################