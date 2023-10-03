from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DB_Doctor, DB_Patient

# Create your views here.
def home(response):
    return render(response, 'dashboard/home.html')

def patients(response):
    patients = DB_Patient.objects.all()
    context = {}
    context['table_html'] = ''''''
    for patient  in patients:
        context['table_html'] += f'''
            <tr>
                <th>{patient.first_name}</th>
                <th>{patient.gender}</th>
                <th>{patient.age}</th>
            </tr>
        '''
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
        patient = DB_Patient(
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
        doctor = DB_Doctor(
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