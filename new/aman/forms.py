from dataclasses import field, fields
from django import forms
from django.forms import Form, ModelForm, DateField, widgets

from aman.clasat.faults import ImageFault
from .models import Item , Visit


###********************************************************###
from aman.format.faults_forms import *
###********************************************************###


###********************************************************###
##############################################################

###### Visit Form Start #####

#### #### #### #### #### ####
class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done','store','send_by','fixed_by','type_of']
        widgets = {
            'date_visit': widgets.DateInput(attrs={'type': 'date'}),
            'item': widgets.SelectMultiple()
        }
class VisitFaultFormAdmen(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['argent',
        'faults',
        ]
        widgets = {
            'faults': widgets.SelectMultiple(),
        }


class VisitFormAdmen(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['store','short_desc',
        'describe_proplem','argent',
        'faults',
        ]
        widgets = {
            'faults': widgets.SelectMultiple(),
        }

class VisitFormStaff(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done']

#### #### #### #### #### ####

###### Visit Form End #####

##############################################################

##############################################################

###### Fault Form Start #####

#### #### #### #### #### ####

#### #### #### #### #### ####

###### Fault Form End #####

##############################################################

##############################################################

###### Item Form Start #####

#### #### #### #### #### ####

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ItemFormAdmen(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','image']

#### #### #### #### #### ####

###### Item Form End #####


##############################################################
###********************************************************###
