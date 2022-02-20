from aman.models import Fault , ImageFault
from django import forms

class FaultImageForm(forms.ModelForm):
    class Meta:
        model = ImageFault
        fields = ['image','describ']
        widgets = {
            'image':forms.widgets.FileInput(attrs={'class':'form-select-multiple multiple'})
        }
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
        'fixed_at','need_to_approve','active_tosend',
        'approved_to_repair','status_choice',
        'action_to_fault','choices_el_status','visit'
        ]
        widgets = {
            'item': forms.widgets.SelectMultiple(attrs={'class':'form-select-multiple'}),
        }
class FaultVisitFormAdmen(forms.ModelForm):
    class Meta:
        model = Fault
        exclude = ['item',
        'status','created_by',
        'created_at','active',
        'fixed_at','need_to_approve',
        'approved_to_repair','action_to_fault',
        'status_choice',
        ]
        widgets = {
            'item': forms.widgets.SelectMultiple(attrs={'class':'form-select-multiple'}),
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
            'item': forms.widgets.SelectMultiple(attrs={'class':'form-select-multiple'}),
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