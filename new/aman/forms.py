from dataclasses import field, fields
from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from .models import Fault, Item , Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done','store','send_by','fixed_by','type_of']
        widgets = {
            'date_visit': widgets.DateInput(attrs={'type': 'date'}),
            'item': widgets.SelectMultiple()
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

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ItemFormAdmen(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','image']
class FaultForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = '__all__'

class FaultFormAdmen(forms.ModelForm):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at','active',
        'fixed_at','need_to_approve',
        'approved_to_repair',
        ]
        widgets = {
            'item': widgets.SelectMultiple(attrs={'class':'form-select-multiple'}),
        }


class FaultFormEmergency(forms.ModelForm):
    class Meta:
        model = Fault
        exclude = [
        'status','created_by',
        'created_at','active',
        'fixed_at','need_to_approve',
        'approved_to_repair','belong_to','visit',
        ]
        widgets = {
            'item': widgets.SelectMultiple(attrs={'class':'form-select-multiple'}),
        }

class FaultFormStaff(forms.ModelForm):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at','fixed_at',
        'active','active_tosend',
        'need_to_approve','approved_to_repair',
        ]