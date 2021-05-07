from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Doctor, Patient, Availability
from ..lib.convert_to_time import convert


# Test User Registration Endpoint
class TestSetCalender(APITestCase):
    def setUp(self):
        self.doctor_data = {
            "first_name": "Mudia",
            "last_name": "Iredia",
            "email": "mudia@gmail.com",
            "phone_number": "2348151107708",
            "password": "mudiareal",
            "department": "OBGYN"
        }
        self.doctor = Doctor.objects.create(**self.doctor_data)

        self.patient_data = {
            "first_name": "Joy",
            "last_name": "Iredia",
            "email": "joy@gmail.com",
            "phone_number": "2348151107708",
            "password": "joyreal"
        }

        self.patient = Patient.objects.create(**self.patient_data)

        self.calender_data = {
            "doctor_id": self.doctor,
            "day": "Monday",
            "start_time": convert(["08", "00"]),
            "end_time": convert(["16", "00"])
        }

        self.calender = Availability.objects.create(**self.calender_data)

        self.book_data = {
            "email": self.patient.email,
            "doctor_email": self.doctor.email,
            "day": "Monday",
            "start_time": "08:00",
            "stop_time": "10:00"
        }

    def test_create_doctor_schedule(self):
        url = reverse('book-appointment')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
