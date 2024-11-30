from django.shortcuts import render , redirect
from .models import *
from .forms import *
from novena.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='account_login')
def dash(request): 
    appoinment = Appoinment.objects.filter(doctor=request.user)
    if request.method=='POST':
        if 'done' in request.POST:
            value = request.POST.get('value')
            Appoinment.objects.filter(id=value).update(status='done')
            return redirect('dash')
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    departement = Departement.objects.all()
    doctor = Doctor.objects.filter(
        Q(departement__name__icontains=q)
    )
    
    context = {'departement':departement , 'doctor':doctor , 'appoinment':appoinment}
    return render(request,'novena_dash/dash.html',context)

def patient(request , username):
    patient = Patient.objects.get(username=username)
    context = {'patient':patient}
    return render(request,'novena_dash/patient.html',context)

@login_required(login_url='account_login')
def contact_patient(request , username , pk):
    patient = Patient.objects.get(username=username)
    doctor = Doctor.objects.get(id=pk)
    message = Message.objects.filter(patient=patient , doctor=doctor)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            patients=form.save(commit=False)
            patients.patient=patient
            patients.doctor=doctor
            patients.save()
          
            
            
            return redirect('contact_patient',username=username , pk=doctor.id)
    context = {'patient':patient,'form':form , 'message':message ,'doctor':doctor}
    return render(request,'novena_dash/contact_patient.html',context)

def doctor_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                password =make_password(form.cleaned_data.get('password1'))
                user = Doctor(username=username,first_name=first_name,last_name=last_name,email=email,password=password , is_doctor=True)
                user.save()
                send_email_confirmation(request,user)
                messages.success(request , 'Please Continue your registration')
                
                return redirect('doctor_signup_finish',user.username)
        else:
            form = DoctorForm()
            messages.error(request,(form.errors.as_text()))

    context = {'form':form}
    return render(request,'novena_dash/doctor_signup.html',context)
 
def doctor_signup_finish(request ,username ):
    doctor = Doctor.objects.get(username=username)
    form = ProfileDoctorForm(instance = doctor)
    if request.method == 'POST':
        user = request.user
        form = ProfileDoctorForm( data=request.POST , files = request.FILES , instance = doctor)
        if form.is_valid():
            doctor_pic = form.cleaned_data['doctor_pic']
            departement = form.cleaned_data['departement']
            certificate = form.cleaned_data['certificate']
            descriptions = form.cleaned_data['descriptions']
            skills = form.cleaned_data['skills']
            expertise_area = form.cleaned_data['expertise_area']
            form.save()
            messages.success(request , 'Congradulation your account was created successfuly')
            return redirect('account_login')
        else :
            form = ProfileDoctorForm()
            messages.error(request,(form.errors.as_text()))
        
    
    return render(request,'novena_dash/doctor_signup_finish.html',{'form':form})

def doctor_single(request , username):
    doctor = Doctor.objects.get(username=username)
    education = My_Educational.objects.filter(doctor=doctor)
    context = {'doctor':doctor , 'education':education}
    return render(request,'novena_dash/doctor_single.html',context)

def add_education(request):
    
    form = AddEducationForm()
    if request.method == 'POST':
        form = AddEducationForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.doctor = request.user.doctor
            doctor.save()
            messages.success(request , 'Congradulation your eduction was add successfuly')
            return redirect('account_profile',request.user.id)
        else :
            form = AddEducationForm()
            messages.warning(request,(form.errors.as_text()))
    context = {'form':form}
    return render(request,'novena_dash/add_education.html',context)

def edit_education(request,pk):
    form = AddEducationForm(instance=My_Educational.objects.get(id=pk))
    if request.method == 'POST':
        form = AddEducationForm(request.POST,instance=My_Educational.objects.get(id=pk))
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.doctor = request.user.doctor
            doctor.save()
            messages.success(request , 'Congradulation your eduction was edit successfuly')
            return redirect('account_profile',request.user.id)
        else :
            form = AddEducationForm(instance=My_Educational.objects.get(id=pk))
            messages.warning(request,(form.errors.as_text()))
    context = {'form':form}
    return render(request , 'novena_dash/edit_education.html', context)

def delete_education(request,pk):
    education = My_Educational.objects.get(id=pk)
    if request.method == 'POST':
        education.delete()
        messages.success(request , 'Congradulation your eduction was deleted successfuly')
        return redirect('account_profile',request.user.id)
    context = {'education':education}
    return render(request,'novena_dash/delete_education.html',context)

