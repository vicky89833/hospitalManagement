from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    license_number = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"
