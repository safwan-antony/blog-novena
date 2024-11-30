from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm , UserCreationForm

class PatientForm(UserCreationForm , UserChangeForm):
    class Meta:
        model = Patient
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  )
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
        
class ProfilePatientForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = (
            'age', 'gender', 'phone','address','city','state','country','medical_history','patient_pic'
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
        labels = {
            'full_name': 'Full Name',
            'age': 'Age',
            'gender': 'Gender',
            'phone': 'Phone',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'medical_history': 'Medical History'
        }

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = ('department','doctor','day', 'time', 'full_name','status', 'message')
        widgets = {
            'day': forms.DateInput(attrs={'class': 'form-control' ,'placeholder': 'yyyy-mm-dd'}),
            'time': forms.TimeInput(attrs={'class': 'form-control' ,'placeholder': 'time'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'full_name'}),
            'status': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'status'}),
            'message': forms.Textarea(attrs={'class': 'form-control' ,'placeholder': 'message'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone', 'subject', 'message')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'full_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' ,'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'subject'}),
            'message':forms.Textarea(attrs={'class': 'form-control' ,'placeholder': 'message'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'subject': 'Subject',
            'message': 'Message',
        }