import os
from django.shortcuts import render
import logging
from .forms import DoctorForm
from .models import Doctor
# Create your views here.
# def login(request):
#     context = {}
#     return render(request, 'SbitarApp/login.html', context)

def login(request):
    context = {}
    template_path = '/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/login.html'

    return render(request, template_path, context)

# def homePage(request):
#     context = {}
#     return render(request, 'SbitarApp/homePage.html', context)
def homePage(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/homePage.html'
    return render(request, template_path, context)
    
def addDoctor(request):
    if request.method == 'POST':
        logging.debug("POST POST POST POST POST POST POST v ")
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            form = DoctorForm()
        logging.debug(request.POST)
        template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/add-doctor.html'
        return render(request, template_path, {'form': form})
    else:
        logging.debug("get get get gte gtegte gtegte")
        context = {}
        template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/add-doctor.html'
        return render(request, template_path, context)


# def add_doctor(request):
#     logging.debug("Form submitted successfully!")
#     if request.method == 'POST':
#         form = DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = DoctorForm()
#             template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/add-doctor.html'
#             return render(request, template_path, {'form': form})
#     else:
#         form = DoctorForm()
#         template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/add-doctor.html'
#     return render(request, template_path, {'form': form})


