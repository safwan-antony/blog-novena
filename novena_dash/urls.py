from django.urls import path
from .views import *


urlpatterns = [
    path('novena-dashboard/',dash,name='dash'),
    path('patinet/<str:username>/',patient,name='patient'),
    path('doctor-signup/',doctor_signup,name='doctor_signup'),
    path('doctor-signup-finish/<str:username>/',doctor_signup_finish,name='doctor_signup_finish'),
    path('doctor-single/<str:username>/',doctor_single,name='doctor_single'),
    path('add-education/',add_education,name='add_education'),
    path('edit-education/<str:pk>/',edit_education,name='edit_education'),
    path('delete-education/<str:pk>/',delete_education,name='delete_education'),
    path('contact-patient/<str:username>/<str:pk>/',contact_patient,name='contact_patient'),
    

]