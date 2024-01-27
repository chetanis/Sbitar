from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('homePage/',views.homePage,name='homePage'),

    path('homePage/add-doctor',views.addDoctor,name='addDoctor'),
    path('homePage/doctors',views.allDoctorsPage,name='doctors'),
    path('homePage/about-doctor/<int:doctor_id>',views.doctorDetails,name='aboutDoc'),

    path('homePage/add-Patient',views.addPatient,name='addPatient'),
    path('homePage/Patients',views.allPatientsPage,name='Patients'),
    path('homePage/about-patient/<int:patient_id>',views.patientDetails,name='consult'),



    path('homePage/add-appointment',views.addAppointments,name='addAppointment'),
    path('homePage/appointments',views.allAppointmentsPage,name='appointments'),

    path('homePage/add-room',views.addRoom,name='addRoom'),
    path('homePage/rooms',views.allRoomsPage,name='rooms'),

]
