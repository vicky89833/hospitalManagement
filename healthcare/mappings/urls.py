from django.urls import path
from .views import (
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingRetrieveDestroyView,
    PatientDoctorMappingsByPatientView
)

urlpatterns = [
    path('', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', PatientDoctorMappingRetrieveDestroyView.as_view(), name='mapping-retrieve-destroy'),
    path('patient/<int:patient_id>/', PatientDoctorMappingsByPatientView.as_view(), name='mappings-by-patient'),
]
