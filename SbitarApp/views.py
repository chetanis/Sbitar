import os
from django.shortcuts import render

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
    context = {}
    template_path ='/Users/anischetouane/Desktop/projet si/attempt 2/sbitar/SbitarApp/templates/homePage.html'
    return render(request, template_path, context)
    

