from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

##forms

class Manual_data_entry(forms.Form):
    entry_Type = forms.ChoiceField(choices=['Incoming Stock', 'Current Stock', 'Outgoing Stock'], required=True, label='Entry Type')
    
    engine_no = forms.CharField(max_length=20)
    vin_number = forms.CharField(max_length = 20)
    

class excel_data_entry(forms.Form):
    file = forms.FileField(required=True)