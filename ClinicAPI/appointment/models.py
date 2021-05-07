from django.db import models
from django.utils import timezone

import uuid
# Create your models here.
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=255)
    department = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, null=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Availability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, null=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
