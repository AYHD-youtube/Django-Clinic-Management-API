from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Doctor


# Test User Registration Endpoint
class TestLoginUser(APITestCase):
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

        self.login_data = {
            "email": "mudia@gmail.com",
            "password": "mudiareal"
        }

        self.wrong_data = {
            "email": "theresa@gmail.com",
            "password": "test12345"
        }

    def test_login_doctor_with_valid_details(self):
        url = reverse('login')
        response = self.client.post(url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_doctor_with_invalid_details(self):
        url = reverse('login')
        response = self.client.post(url, self.wrong_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
