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

class VisitFormStaff(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['done']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class FaultForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = '__all__'