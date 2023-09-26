from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response, 'dashboard/home.html')



def add_patient(response):
    if response.method == "POST":
        return redirect("/")
    else:
        return render(response, 'dashboard/add_patient.html')