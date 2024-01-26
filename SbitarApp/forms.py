# forms.py
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'last_name', 'specialty', 'phone_number',]
