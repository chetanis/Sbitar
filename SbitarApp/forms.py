# forms.py
from django import forms
from .models import Doctor, Patient,Appointment, Result, RoomAllotment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'last_name', 'departement', 'title', 'email', 'gender', 'phone_number', 'dob']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'last_name', 'address', 'email', 'gender', 'phone_number', 'dob']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'service', 'doctor', 'appointment_date', 'time_slot', 'hospitalization', 'problem']

class RoomAllotmentForm(forms.ModelForm):
    class Meta:
        model = RoomAllotment
        fields = ['room_number', 'room_type', 'allotment_date', 'discharge_date', 'appointment']
    
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['appointment', 'diagnostique', 'traitement']