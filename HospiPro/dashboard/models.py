from django.db.models import Q
from django.db import models
from django.core.validators import RegexValidator

class BillItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Enter a valid mobile number.')])
    emergency_contact = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Enter a valid emergency contact number.')])
    medical_license_number = models.PositiveIntegerField()
    specialty = models.CharField(max_length=50)
    availability = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def search(q):
        search_query = (Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(gender__icontains=q) | 
                        Q(mobile_number__icontains=q) | Q(emergency_contact__icontains=q) | Q(address__icontains=q) | 
                        Q(medical_license_number__icontains=q) | Q(specialty__icontains=q) | Q(availability__icontains=q) |
                        Q(age__icontains=q) | Q(email__icontains=q) | Q(experience__icontains=q)
        )
        return Doctor.objects.filter(search_query)
    

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    room_no = models.PositiveIntegerField()
    email = models.EmailField()
    blood_group = models.CharField(max_length=4)
    billing = models.ManyToManyField(BillItem, related_name="bills")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def search(q):
        search_query = (Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(gender__icontains=q) | 
                        Q(mobile_number__icontains=q) | Q(emergency_contact__icontains=q) | Q(address__icontains=q) | 
                        Q(age__icontains=q) | Q(room_no__icontains=q) | Q(blood_group__icontains=q)
        )
        return Patient.objects.filter(search_query)
    

