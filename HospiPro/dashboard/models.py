from django.db import models
from django.core.validators import RegexValidator


class DB_Doctor(models.Model):
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

