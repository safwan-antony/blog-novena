from django.urls import path
from .views import *

urlpatterns = [
    
    path('chek-point/',checkpoint,name='checkpoint'),
    path('patient-signup/',patient_signup,name='patient_signup'),
    path('patient-signup-finish/<str:username>/',patient_signup_finish,name='patient_signup_finish'),
    path('make-appoinment/',make_appoinment,name='make_appoinment'),
    path('confirmation/',confirmation,name='confirmation'),
    path('novena-dashboard/<str:pk>/',delete_appoinment,name='done'),
    path('edit-appoinment/<str:pk>/',edit_appoinment,name='edit-appoinment'),
    path('contact-us/',contact,name='contact'),
    path('about/',about,name='about'),
    path('our-service/',service,name='service'),
    path('department/',department,name='department'),
    path('department-details/<str:name>/',department_details,name='department_details'),
    path('doctor/',doctor,name='doctor'),
    
]