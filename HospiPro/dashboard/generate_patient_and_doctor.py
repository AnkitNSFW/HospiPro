from .models import Doctor, Patient
import random
from faker import Faker          
fake = Faker() 


def generate_patient(num):
    try:
        for _ in range(num):
            Patient(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                gender=random.choice(['Male','Female','Transgender']),
                mobile_number=random.randint(111111111, 9999999999),
                emergency_contact=random.randint(111111111, 9999999999),
                address=fake.address(),
                age=random.randint(0,100),
                room_no=random.randint(0,50),
                email=fake.email(),
                blood_group=random.choice(['A+','A-','B+','B-','AB+','AB-','O+','O-']),
                bill=0.0,
                paid_bill=0.0
            ).save()
        return True
    except:
        return False

def generate_doctor(num):
    try: 
        for _ in range(num):
            Doctor(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                gender=random.choice(['Male','Female','Transgender']),
                mobile_number=random.randint(111111111, 9999999999),
                emergency_contact=random.randint(111111111, 9999999999),
                medical_license_number=random.randint(1111, 99999),
                specialty=random.choice(['General','Pediatrics','Cardiology','Orthopedics','Obstetrics and Gynecology','Neurology']),
                availability=random.choice(['Full-time','Part-time','Shifts']),
                address=fake.address(),
                email=fake.email(),
                age=random.randint(0,100),
                experience=random.randint(0,20)
            ).save()
        return True
    except:
        return False

def delete_patients():
    try:
        Patient.objects.all().delete()
        return True
    except:
        return False
    
def delete_doctors():
    try:
        Doctor.objects.all().delete()
        return True
    except:
        return False

def delete_individual_user(id):
    try:
        patient = Patient.objects.get(id=id)
        patient.delete()
        return True
    except:
        return False