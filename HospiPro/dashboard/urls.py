from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_patient', views.add_patient, name='add_patient'),
]