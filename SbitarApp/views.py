from datetime import date
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render
import logging
from .forms import DoctorForm, PatientForm,AppointmentForm, RoomAllotmentForm
from .models import Appointment, Doctor, Patient, RoomAllotment
# Create your views here.
def calculate_age(birth_date, current_date):
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age

def login(request):
    context = {}
    template_path = 'login.html'

    return render(request, template_path, context)

def homePage(request):
    doctors = Doctor.objects.all()

    nb_doctors = Doctor.objects.count()
    nb_patients = Patient.objects.count()
    nb_appointmets = Appointment.objects.count()
    
    today_date = timezone.now().date()
    todayAppointments = Appointment.objects.filter(appointment_date = today_date)
    context = {'doctors': doctors,'appointments': todayAppointments,'nb_doctors':nb_doctors,'nb_patients':nb_patients,'nb_appointmets':nb_appointmets}
    template_path ='homePage.html'
    return render(request, template_path, context)

def allDoctorsPage(request):
    doctors = Doctor.objects.all()
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
    
def doctorDetails(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    context = {'doctor': doctor}
    template_path ='about-doctor.html'
    return render(request, template_path, context)



def allPatientsPage(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    template_path ='patients.html'
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

def patientDetails(request,patient_id):
    patient = Patient.objects.get(id=patient_id)
    birth_date = patient.dob
    current_date = date.today()
    age = calculate_age(birth_date, current_date)
    context = {'patient': patient,'age':age}
    template_path ='about-patient.html'
    return render(request, template_path, context)


def allAppointmentsPage(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    template_path ='appointments.html'
    return render(request, template_path, context)

def addAppointments(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    context = {'patients': patients,'doctors': doctors}
    template_path ='add-appointment.html'
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppointmentForm()
            messages.success(request, 'appointment added successfully!')
        else:
            messages.error(request, 'Form submission error.')
        return render(request, template_path, {'patients': patients,'form': form,'doctors': doctors})
    
    return render(request, template_path, context)



def allRoomsPage(request):
    rooms = RoomAllotment.objects.all()
    context = {'rooms': rooms}
    template_path ='rooms.html'
    return render(request, template_path, context)

def allotRoom(request):
    template_path ='add-room.html'
    appointments = Appointment.objects.filter(status='pending')
    context = {'appointments': appointments}
    if request.method == 'POST':
        form = RoomAllotmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = RoomAllotmentForm()
            messages.success(request, 'appointment added successfully!')
        else:
            logging.debug(form.errors)
            messages.error(request, 'Form submission error.')
    return render(request, template_path, context)