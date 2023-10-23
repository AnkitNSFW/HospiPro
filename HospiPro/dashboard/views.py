from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor, Patient, BillItem
from .generate_patient_and_doctor import *



# Create your views here.
def home(response):
    return render(response, 'dashboard/home.html')

def patients(response):
    context = {}
    context['patients'] = Patient.objects.all()
    return render(response, 'dashboard/patient/patients.html', context=context)

def patients_id(response, id):
    context = {}
    context['patient'] = None
    try:
        context['patient'] = Patient.objects.get(id=id)
    except:
        context['patient'] = []
    print(id)
    return render(response, 'dashboard/patient/individual_patient.html', context=context)

# if someone directly goes to /search/ without to_srarch redirecting to /patient
def patients_search(response):
    return redirect('patients')

def patients_to_search(response, to_search):
    context = {}
    try:
        context['patients'] = Patient.search(to_search)
    except:
        context['patients'] = []

    return render(response, 'dashboard/patient/patients.html', context=context)

def doctors(response):
    context = {}
    context['doctors'] = Doctor.objects.all()
    return render(response, 'dashboard/doctor/doctors.html', context=context)

def doctors_id(response, id):
    context = {}
    context['doctor'] = None
    try:
        context['doctor'] = Doctor.objects.get(id=id)
    except:
        context['doctor'] = []
    print(id)
    return render(response, 'dashboard/doctor/individual_doctor.html', context=context)

# if someone directly goes to /search/ without to_srarch redirecting to /doctor
def doctors_search(response):
    return redirect('doctors')

def doctors_to_search(response, to_search):
    print(to_search)
    context = {}
    # try:
    #     context['doctors'] = Doctor.search(to_search)
    # except:
    #     context['doctors'] = []
    context['doctors'] = Doctor.search(to_search)
    return render(response, 'dashboard/doctor/doctors.html', context=context)

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
            blood_group=blood_group,
            paid_bill=0,
            total_bill=0
        )
        patient.save()
        return redirect("/")
    else:
        return render(response, 'dashboard/patient/add_patient.html')
    
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
        return render(response, 'dashboard/doctor/add_doctor.html')

def something_went_wrong(response):
    return render(response, 'dashboard/something_went_wrong.html')

def delete_patient(response, id):
    if delete_individual_user(id=id):
        return redirect('/patients')
    else:
        return redirect('/something_went_wrong')


def billing(response):
    context = {}
    context["patients"] = []
    for patient in Patient.objects.all():
        update_total_bill(patient.id)
        context["patients"].append(
            {"id": patient.id,
            "name": patient.first_name+" "+patient.last_name,
            "gender": patient.gender,
            "mobile_number": patient.mobile_number,
            "total_bill": patient.total_bill,
            "paid_bill": patient.paid_bill,
            "balance": patient.total_bill - patient.paid_bill
            }
        )

    return render(response, 'dashboard/billing/billing.html' ,context=context)

def individual_billing(response, id):
    try:
        context = {}
        update_total_bill(id=id)
        patient = Patient.objects.get(id=id)
        context['patient']=patient
        
        if patient:
            context['total_bill'], context['item_list'] = patients_bill_items(id=id)
            context['balance'] = patient.paid_bill-patient.total_bill
            return render(response, 'dashboard/billing/individual_billing.html' ,context=context)
        else:
            return redirect('/something_went_wrong')
    except:
        return redirect('/something_went_wrong')

def add_to_bill(response, id):
    try:
        if response.method == 'GET':
            context = {}
            context['patient_id']=id
            return render(response, 'dashboard/billing/billing_add_to_bill.html', context=context)
        elif response.method == 'POST':
            BillItem(
                patient_id=id,
                name=response.POST['name'],
                description=response.POST['description'],
                cost=response.POST['cost']
            ).save()
            return redirect(f'/billing/{id}')
    except:
        return redirect('/something_went_wrong')

def pay_bill(response, id):
    try:
        if response.method == 'GET':
            update_total_bill(id=id)
            patient = Patient.objects.get(id=id)
            context = {}
            context['patient_name'] = patient.first_name+" "+patient.last_name
            context['patient_id'] = patient.id
            context['total_bill'] = patient.total_bill
            context['paid_bill'] = patient.paid_bill
            context['balance'] = patient.paid_bill-patient.total_bill

            return render(response, 'dashboard/billing/billing_pay_bill.html', context=context)
        elif response.method == 'POST':
            patient = Patient.objects.get(id=id)
            patient.paid_bill += int(response.POST['paid_amount'])
            patient.save()
            return redirect(f'/billing/{id}')
    except:
        return redirect('/something_went_wrong')

# temp things
def api_add_patient(response, num):
    if generate_patient(num):
        return redirect('/patients')
    # else:
    #     return redirect('/something_went_wrong')

def api_add_doctor(response, num):
    if generate_doctor(num):
        return redirect('/doctors')
    else:
        return redirect('/something_went_wrong')

def delete_all_patient(response):
    if delete_patients():
        return redirect('/patients')
    else:
        return redirect('/something_went_wrong')

def delete_all_doctor(response):
    if delete_doctors():
        return redirect('/doctors')
    else:
        return redirect('/something_went_wrong')


def test_api_call(response):
    return redirect('/')