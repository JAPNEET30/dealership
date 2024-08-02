from distutils.command import upload
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, FileExtensionValidator
from django.contrib.auth import get_user_model
from .models import *

##forms
#for vehicle entry
class vehicle_manual_entry(forms.Form):
    engine_no = forms.CharField(max_length=20)
    vin_number = forms.CharField(max_length = 20)
    model_name = forms.ChoiceField()
    class Meta:
        model = vehicle_entry
        fields = ('invoice_no', 'invoice_date', 'model_name', '')
        REQUIRED_FIELDS = []
    
#for vehicle entry
class vehicle_excel_entry(forms.Form):
    file = forms.FileField(required=True, validators = [FileExtensionValidator(['xlsx','xls'], message='Uploaded File is not of the supported Extension')])

#for category and location entries
class category_upload_entry(forms.Form):
    cat_file = forms.FileField(allow_empty_file=False, required=True, validators=[FileExtensionValidator(['xlsx','xls'])], help_text='Please upload \'.xlsx\' or \'.xls\' file only')

class category_manual_entry(forms.Form):
    model_name = forms.CharField(max_length=20, required = True)
    colors = forms.CharField(max_length=100)
    varients = forms.CharField(max_length=100)
    is_accessories_included = forms.BooleanField(label= 'Accessories Included')
    accessories_listed = forms.CharField(max_length=100)

class location_manual_entry(forms.Form):
    name=forms.CharField(max_length=20, required=True)
    tag = forms.CharField(max_length = 20, required=False)
    address = forms.CharField(max_length=100, required=True)
    type = forms.ChoiceField(choices={'storage':'Storage', 'point_of_sale':'Point of Sale', 'both':'Both'})