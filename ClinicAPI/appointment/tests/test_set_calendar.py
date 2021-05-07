from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Doctor
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

        self.calender_data = {
            "email": self.doctor.email,
            "day": "Monday",
            "open": convert(["08", "00"]),
            "closed": convert(["16", "00"])
        }

    def test_create_doctor_schedule(self):
        url = reverse('set-calender')
        response = self.client.post(url, self.calender_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
