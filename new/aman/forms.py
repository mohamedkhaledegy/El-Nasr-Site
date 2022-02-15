from dataclasses import field, fields
from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from .models import Fault, Item , Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done','store']
        widgets = {
            'date_visit': widgets.DateInput(attrs={'type': 'date'}),
            'content': widgets.SelectMultiple()
        }
class VisitFormAdmin(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['store','short_desc',
        'describe_proplem','argent',
        'faults'
        ]

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

class FaultFormStaff(forms.ModelForm):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at','fixed_at',
        'active','active_tosend',
        'need_to_approve','approved_to_repair',
        ]