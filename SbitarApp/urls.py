from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login/',views.chekLogin,name='loginCheck'),
    path('homePage/',views.homePage,name='homePage'),

    path('homePage/add-doctor',views.addDoctor,name='addDoctor'),
    path('homePage/doctors',views.allDoctorsPage,name='doctors'),
    path('homePage/about-doctor/<int:doctor_id>',views.doctorDetails,name='aboutDoc'),
    path('update-doctor/<int:doctor_id>/', views.updateDoctor, name='updateDoctor'),
    path('delete-doctor/<int:doctor_id>/', views.deleteDoctor, name='deleteDoctor'),

    path('homePage/add-Patient',views.addPatient,name='addPatient'),
    path('homePage/Patients',views.allPatientsPage,name='Patients'),
    path('homePage/about-patient/<int:patient_id>',views.patientDetails,name='consult'),
    path('delete-patient/<int:patient_id>/', views.deletePatient, name='deletePatient'),
    path('update-patient/<int:patient_id>/', views.updatePatient, name='updatePatient'),


    path('homePage/add-appointment',views.addAppointments,name='addAppointment'),
    path('homePage/appointments',views.allAppointmentsPage,name='appointments'),

    path('homePage/add-room',views.allotRoom,name='addRoom'),
    path('homePage/rooms',views.allRoomsPage,name='rooms'),

    path('homePage/result',views.addResult,name='result'),

]
