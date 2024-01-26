from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('homePage/',views.homePage,name='homePage'),

    path('homePage/add-doctor',views.addDoctor,name='addDoctor'),
    path('homePage/doctors',views.allDoctorsPage,name='doctors'),

    path('homePage/add-Patient',views.addPatient,name='addPatient'),
    path('homePage/Patients',views.allPatientsPage,name='Patients'),

    path('homePage/add-appointment',views.addAppointments,name='addAppointment'),
    path('homePage/appointments',views.allAppointmentsPage,name='appointments'),

]
