from django import forms
from django.core.exceptions import ValidationError
from taxi.models import Driver, Car
import re


def validate_license_number(value):
    pattern = r"^[A-Z]{3}\d{5}$"
    if not re.match(pattern, value):
        raise ValidationError(
            "License number must contain 3 uppercase letters and 5 digits"
        )


class DriverCreateForm(forms.ModelForm):
    license_number = forms.CharField(validators=[validate_license_number])

    class Meta:
        model = Driver
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "license_number",
        )
        widgets = {
            "password": forms.PasswordInput(),
        }

class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(validators=[validate_license_number])

    class Meta:
        model = Driver
        fields = ("license_number",)


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }