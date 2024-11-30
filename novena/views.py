from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from a_users.views import *
from django .db.models import Q



# Create your views here.


def home(request):
    return render(request,'novena/home.html')

def checkpoint(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'novena/checkpoint.html')
    
def patient_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                password =make_password(form.cleaned_data.get('password1'))
                user = Patient(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                send_email_confirmation(request,user)
                messages.success(request , 'Please Continue your registration')
                
                return redirect('patient_signup_finish',user.username)
            else :
                form - PatientForm()
                messages.error(request , 'Password does not match')
        else:
            form = PatientForm()
            messages.error(request,(form.errors.as_text()))
    context = {'form':form}
    return render(request,'novena/patient_signup.html',context)

def patient_signup_finish(request , username):
    if request.user.is_authenticated:
        return redirect('home')
    patient = Patient.objects.get(username=username)
    form = ProfilePatientForm(instance = patient)
    if request.method == 'POST':
        user = request.user
        form = ProfilePatientForm( data=request.POST , files = request.FILES , instance = patient)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            medical_history = form.cleaned_data['medical_history']
            patient_pic = form.cleaned_data['patient_pic']
            form.save()
            
            messages.success(request , 'Congradulation your account was complate successfuly')
            return redirect('account_login')
        else :
            form = ProfilePatientForm()
            messages.error(request,(form.errors.as_text()))
        
    context = {'form':form}
    return render(request,'novena/patient_signup_finish.html',context)

@login_required(login_url='account_login')
def make_appoinment(request):
    appoinment = Appoinment.objects.all()
    form = AppoinmentForm()
    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            appoinment=form.save(commit=False)
            appoinment.patient = request.user.patient
            appoinment.save() 
            messages.success(request , 'Congradulation your appoinment was created successfuly the doctor will talk with you soon')
            return redirect('confirmation')
        else :
            messages.error(request,(form.errors.as_text()))
    context = {'appoinment':appoinment , 'form':form}
    return render(request,'novena/make_appoinment.html',context)

@login_required(login_url='account_login')
def confirmation(request):
    return render(request,'novena/confirmation.html')

@login_required(login_url='account_login')
def edit_appoinment(request , pk):
    appoinment = Appoinment.objects.get(id=pk)
    form = AppoinmentForm(instance=appoinment)
    if request.method == 'POST':
        form = AppoinmentForm(request.POST , instance=appoinment)
        if form.is_valid():
            form.save()
            return redirect('account_profile', request.user.id)
        else :
            form = AppoinmentForm(request.POST , instance=appoinment)
            messages.error(request,(form.errors.as_text()))
    context = {'form':form}
    return render(request , 'novena/edit-appoinment.html',context)
def delete_appoinment(request,pk):
    appoinment = Appoinment.objects.get(id=pk)
    appoinment.delete()
    if request.user.is_doctor:
        return redirect('dash')
    else:
        return redirect('account_profile', request.user.id)
    

@login_required(login_url='account_login')
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'Thank you for your message we will contact you soon')
            return redirect('home')
        else :
            form = ContactForm()
            messages.error(request,(form.errors.as_text()))
    context = {'form':form}
    return render(request,'novena/contact.html',context)

def about(request):
    doctor = User.objects.filter(is_doctor=True)
    context = {'doctor':doctor}
    return render(request,'novena/about.html',context)

def service(request):
    return render(request,'novena/service.html')

def department(request):
    department = Departement.objects.all()
    context = {'department':department}
    return render(request,'novena/department.html',context)
def department_details(request,name):
    department = Departement.objects.get(name=name)
    context = {'department':department}
    return render(request , 'novena/department-detail.html',context)


def doctor(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    department = Departement.objects.all()
    doctor = User.objects.filter(is_doctor=True , doctor__departement__name__icontains=q)
    context = {'doctor':doctor,'department':department}
    return render(request,'novena/doctor.html',context)