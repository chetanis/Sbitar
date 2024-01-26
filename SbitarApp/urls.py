from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('homePage/',views.homePage,name='homePage'),
    path('homePage/add-doctor',views.addDoctor,name='addDoctor'),
    # path('homePage/fff',views.add_doctor,name='add_doctor'),

]
