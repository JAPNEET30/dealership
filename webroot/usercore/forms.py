from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
from .models import User


def validate_phone(value):
    if len(str(value))==10:
        raise ValidationError(
            _("%(value)s is not a phone number"),
            params={"value": value},
        )

class registrationForm(UserCreationForm):
    last_name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'phone_contact', 'email', 'businessName', 'gstin_Number')
        REQUIRED_FIELDS=["email", 'username', 'password1', 'password2', 'first_name', 'phone_contact', 'businessName']
        
    