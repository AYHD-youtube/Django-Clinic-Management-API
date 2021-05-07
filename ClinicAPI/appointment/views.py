from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .lib.lower_strip import strip_and_lower
from .lib.convert_to_time import convert
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Login View
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = strip_and_lower(request.data.get('email', ''))
            password = request.data.get('password', '')

            if email is None or password is None:
                return Response(
                    dict(invalid_credential='Please provide both email and password'),
                    status=status.HTTP_400_BAD_REQUEST)

            try:
                user_type = Doctor.objects.get(email=email)
            except Exception:
                user_type = Patient.objects.get(email=email)

            if isinstance(user_type, Doctor) and password == Doctor.objects.get(email=email).password:
                doctor = Doctor.objects.get(email=email)

                if not doctor:
                    return Response(
                        dict(invalid_credential='Please ensure that your email and password are correct'),
                        status=status.HTTP_400_BAD_REQUEST)

                return Response(dict(message=f"Welcome Doctor {doctor.first_name}"), status=status.HTTP_200_OK)

            if isinstance(user_type, Patient) and password == Patient.objects.get(email=email).password:
                patient = Patient.objects.get(email=email)

                if not patient:
                    return Response(
                        dict(invalid_credential='Please ensure that your email and password are correct'),
                        status=status.HTTP_400_BAD_REQUEST)

                return Response(dict(message=f"Welcome {patient.first_name}"), status=status.HTTP_200_OK)

            else:
                return Response(
                    dict(invalid_credential='This Email does not exist in our records'),
                    status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(
                dict(invalid_credential='This Email does not exist in our records'),
                status=status.HTTP_400_BAD_REQUEST)
# Set Calender Availability View
class Calender(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = strip_and_lower(request.data.get('email', ''))
        day = str.capitalize(request.data.get('day', ''))
        start_time = request.data.get('open', '').split(":")
        closing_time = request.data.get('closed', '').split(":")

        try:
            doctor = Doctor.objects.get(email=email)
            doctor_id = doctor.id

            calender_data = {
                "doctor_id": doctor_id,
                "day": day,
                "start_time": convert(start_time),
                "end_time": convert(closing_time)
            }

            calender_serializer = AvailabilitySerializer(data=calender_data)
            if calender_serializer.is_valid():
                calender_serializer.save()
            else:
                return Response(
                    dict(calender_serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST)

            return Response(dict(message="Calender Availability is set"), status=status.HTTP_201_CREATED)

        except Exception:
            return Response(
                dict(invalid_credential='Sorry, You are not a Doctor.'),
                status=status.HTTP_400_BAD_REQUEST)


class BookAppointment(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        patient_email = strip_and_lower(request.data.get('email', ''))
        doctor_email = strip_and_lower(request.data.get('doctor_email', ''))
        day = str.capitalize(request.data.get('day', ''))
        start_time = convert(request.data.get('start_time', '').split(":"))
        end_time = convert(request.data.get('stop_time', '').split(":"))

        try:
            patient = Patient.objects.get(email=patient_email)
            patient_id = patient.id

            try:
                doctor_id = Doctor.objects.get(email=doctor_email).id

            except Exception:
                return Response(dict(message="The Doctor you have selected does not exist."))

            # Validate selected time with Doctor's availability.
            doctor_availability = Availability.objects.get(doctor_id=doctor_id, day=day)

            if start_time < doctor_availability.start_time or end_time > doctor_availability.end_time:
                return Response(dict(
                    invalid_credential='Sorry, The Doctor you have selected is not available at this time.'),
                    status=status.HTTP_400_BAD_REQUEST)

            if doctor_availability.start_time <= start_time or doctor_availability.end_time >= end_time:

                # check if the time has been booked by another patient
                try:

                    appointments_day = Appointment.objects.filter(day=day)
                    for value in appointments_day:

                        if value.start_time == start_time and value.end_time == end_time:
                            return Response(dict(message="The time slot you have selected has already been booked."))

                        if value.start_time <= start_time <= value.end_time:
                            return Response(dict(message="The time slot you have selected has already been booked."))

                        if value.start_time <= end_time <= value.end_time:
                            return Response(dict(message="The time slot you have selected has already been booked."))

                        if start_time <= value.start_time and end_time >= value.end_time:
                            return Response(dict(message="The time slot you have selected has already been booked."))

                    appointment_data = {
                        "patient_id": patient_id,
                        "doctor_id": doctor_id,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time
                    }

                    appointment_serializer = AppointmentSerializer(data=appointment_data)

                    if appointment_serializer.is_valid():
                        appointment_serializer.save()
                    else:
                        return Response(
                            dict(appointment_serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)
                    return Response(dict(message="Appointment has been Booked successfully"),
                                    status=status.HTTP_201_CREATED)

                except Exception:

                    appointment_data = {
                        "patient_id": patient_id,
                        "doctor_id": doctor_id,
                        "day": day,
                        "start_time": start_time,
                        "end_time": end_time
                    }

                    appointment_serializer = AppointmentSerializer(data=appointment_data)

                    if appointment_serializer.is_valid():
                        appointment_serializer.save()
                    else:
                        return Response(
                            dict(appointment_serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)
                    return Response(dict(message="Appointment has been Booked successfully"),
                                    status=status.HTTP_201_CREATED)

            return Response(
                dict(invalid_credential='Sorry, The Doctor you have selected is not available at this time.'),
                status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(
                dict(invalid_credential='Sorry, You are not a Registered Patient.'),
                status=status.HTTP_400_BAD_REQUEST)
