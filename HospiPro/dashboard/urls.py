from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('patients', views.patients, name='patients'),
    path('patients/search', views.patients_search, name='patients_search'),
    path('patients/search/<to_search>', views.patients_to_search, name='patients_to_search'),
    path('patients/<int:id>', views.patients_id, name='patients_id'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('patients/delete/<int:id>', views.delete_patient, name='delete_patient'),

    path('doctors', views.doctors, name='doctors'),
    path('doctors/search', views.doctors_search, name='doctors_search'),
    path('doctors/search/<to_search>', views.doctors_to_search, name='doctors_to_search'),
    path('doctors/<int:id>', views.doctors_id, name='doctors_id'),
    path('add_doctor', views.add_doctor, name='add_doctor'),

    path('billing', views.billing, name='billing'),
    path('billing/<int:id>', views.individual_billing, name='individual_billing'),

    path('something_went_wrong', views.something_went_wrong, name='something_went_wrong'),


    path('api_add_patient/<int:num>', views.api_add_patient, name='api_patinet'),
    path('delete_all_patient', views.delete_all_patient, name='delete_all_patinet'),
    path('api_add_doctor/<int:num>', views.api_add_doctor, name='api_doctor'),
    path('delete_all_doctor', views.delete_all_doctor, name='delete_all_doctor'),

    path('test_api_call', views.test_api_call, name='test_api_call'),
]