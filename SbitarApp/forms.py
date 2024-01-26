# forms.py
from django import forms
from .models import Doctor, Patient,Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'last_name', 'specialty', 'experience', 'email', 'gender', 'phone_number', 'dob']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'last_name', 'address', 'email', 'gender', 'phone_number', 'dob']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'service', 'doctor', 'appointment_date', 'time_slot', 'hospitalization', 'problem']