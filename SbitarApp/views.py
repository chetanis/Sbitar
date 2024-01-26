import os
from django.contrib import messages
from django.shortcuts import render
import logging
from .forms import DoctorForm, PatientForm,AppointmentForm
from .models import Appointment, Doctor, Patient
# Create your views here.

def login(request):
    context = {}
    template_path = 'login.html'

    return render(request, template_path, context)

def homePage(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    template_path ='homePage.html'
    return render(request, template_path, context)

def allDoctorsPage(request):
    doctors = Doctor.objects.all()
    for doctor in doctors:
        logging.debug(doctor.email)
    context = {'doctors': doctors}
    template_path ='doctors.html'
    return render(request, template_path, context)

    
def addDoctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            form = DoctorForm()
            messages.success(request, 'Doctor added successfully!')
        else:
            messages.error(request, 'Form submission error. Please correct the errors below.')
        template_path ='add-doctor.html'
        return render(request, template_path, {'form': form})
    else:
        context = {}
        template_path ='add-doctor.html'
        return render(request, template_path, context)



def allPatientsPage(request):
    patients = Patient.objects.all()
    for patient in patients:
        logging.debug(patient.name)
    context = {'patients': patients}
    template_path ='patients.html'
    logging.debug(context)
    return render(request, template_path, context)

def addPatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            form = PatientForm()
            messages.success(request, 'Patient added successfully!')
        else:
            messages.error(request, 'Form submission error. Please correct the errors below.')
        template_path ='add-patient.html'
        return render(request, template_path, {'form': form})
    else:
        context = {}
        template_path ='add-patient.html'
        return render(request, template_path, context)

def allAppointmentsPage(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    template_path ='appointments.html'
    return render(request, template_path, context)

def addAppointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppointmentForm()
            messages.success(request, 'appointment added successfully!')
        else:
            messages.error(request, 'Form submission error.')
        template_path ='add-appointment.html'
        return render(request, template_path, {'form': form})
    else:
        context = {}
        template_path ='add-appointment.html'
        return render(request, template_path, context)