from dataclasses import field, fields
from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from .models import Item , Visit

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
        exclude = ['done','store','fixed_by','send_by','date_visit','created_by','argent']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'