from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor, Patient

import random
from faker import Faker          
fake = Faker() 
fake.random.seed(69420)


# Create your views here.
def home(response):
    return render(response, 'dashboard/home.html')

def patients(response):
    context = {}
    context['patients'] = Patient.objects.all()
    context['individual_patient'] = None
    context['user_not_found'] = False
    return render(response, 'dashboard/patients.html', context=context)

def patients_id(response, id):
    context = {}
    context['patients'] = None
    try:
        context['individual_patient'] = Patient.objects.get(id=id)
        context['user_not_found'] = False
    except:
        context['individual_patient'] = []
        context['user_not_found'] = True

    return render(response, 'dashboard/patients.html', context=context)

def patients_search(response):
    return redirect('patients')

def patients_to_search(response, to_search):
    context = {}
    context['individual_patient'] = None
    try:
        context['patients'] = Patient.search(to_search)
        context['user_not_found'] = False
    except:
        context['patients'] = []
        context['user_not_found'] = True

    return render(response, 'dashboard/patients.html', context=context)


def add_patient(response):
    if response.method == "POST":
        first_name = response.POST['first_name']
        last_name = response.POST['last_name']
        gender = response.POST['gender']
        mobile_number = response.POST['mobile_number']
        emergency_contact = response.POST['emergency_contact']
        address = response.POST['address']
        age = response.POST['age']
        room_no = response.POST['room_no']
        email = response.POST['email']
        blood_group = response.POST['blood_group']

        # Create a new Patient instance and save it to the database
        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            mobile_number=mobile_number,
            emergency_contact=emergency_contact,
            address=address,
            age=age,
            room_no=room_no,
            email=email,
            blood_group=blood_group
        )
        patient.save()
        return redirect("/")
    else:
        return render(response, 'dashboard/add_patient.html')
    
def add_doctor(response):
    if response.method == "POST":
        first_name = response.POST['first_name']
        last_name = response.POST['last_name']
        gender = response.POST['gender']
        mobile_number = response.POST['mobile_number']
        emergency_contact = response.POST['emergency_contact']
        medical_license_number = response.POST['medical_licence_numbar']
        specialty = response.POST['specialty']
        availability = response.POST['availability']
        address = response.POST['address']
        age = response.POST['age']
        email = response.POST['email']
        experience = response.POST['experience']

        print(first_name, gender)

        # Create a new Doctor instance and save it to the database
        doctor = Doctor(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            mobile_number=mobile_number,
            emergency_contact=emergency_contact,
            medical_license_number=medical_license_number,
            specialty=specialty,
            availability=availability,
            address=address,
            age=age,
            email=email,
            experience=experience
        )
        doctor.save()

        return redirect("/")
    else:
        return render(response, 'dashboard/add_doctor.html')


def api_add_patient(response):
    # Create a new Patient instance and save it to the database
    for _ in range(5):
        patient = Patient(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=random.choice(['Male','Female','Transgender']),
            mobile_number=random.randint(111111111, 9999999999),
            emergency_contact=random.randint(111111111, 9999999999),
            address=fake.address(),
            age=random.randint(0,100),
            room_no=random.randint(0,50),
            email=fake.email(),
            blood_group=random.choice(['A+','A-','B+','B-','AB+','AB-','O+','O-'])
        )
        patient.save()

    return render(response, 'dashboard/home.html')

def delete_all_patient(response):
    for patient in Patient.objects.all():
        patient.delete()
    
    return render(response, 'dashboard/home.html')