from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from novena.models import Message


class DoctorForm(UserCreationForm , UserChangeForm):
    class Meta :
        model = Doctor
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class':'form-control', 'placeholder': 'Enter The Username' ,'required': 'required'}),
            'first_name': forms.TextInput(
                attrs={'class':'form-control' ,'placeholder': 'Enter The First Name' , 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class':'form-control', 'placeholder': 'Enter The Last Name' , 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'class':'form-control', 'placeholder': 'Enter The Email' , 'required': 'required'}),
            'password1': forms.PasswordInput(
                attrs={'class':'form-control', 'placeholder': 'Enter The Password' , 'required': 'required'}),
            'password2': forms.PasswordInput(
                attrs={'class':'form-control', 'placeholder': 'Confirm The Password' , 'required': 'required'}),
          
        }
class ProfileDoctorForm(UserChangeForm):
    class Meta:
        model = Doctor
        fields = (
            'doctor_pic','departement','certificate','descriptions','skills','expertise_area'
        )
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your age' }),
            'gender': forms.TextInput(attrs={'class': 'form-control','placeholder': 'gender'}),
            'phone': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'address'}),
            'city': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'city'}),
            'state': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'state'}),
            'country': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'country'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control' ,'placeholder': 'medical_history'}),
            'patient_pic': forms.FileInput(attrs={'class': 'form-control'})
        }

class AddEducationForm(forms.ModelForm):
    class Meta:
        model = My_Educational
        fields = ('degree','university','expertise_area','year','descript')
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'degree'}),
            'university': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'university'}),
            'expertise_area': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'expertise_area'}),
            'year':forms.NumberInput(attrs={'class': 'form-control' ,'placeholder': 'year'}),
            'descript': forms.Textarea(attrs={'class': 'form-control' ,'placeholder': 'descript'})
        }
        labels = {
            'degree': 'Degree',
            'university': 'University',
            'expertise_area': 'Expertise Area',
            'year': 'Year',
            'descript': 'Description'
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control' ,'placeholder': 'Message'})
        }
        labels = {
            'body': 'Message'
        }

