from rest_framework import serializers
from .models import Availability, Appointment,Patient

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields='__all__'
    def validate(self,attrs):
        email= attrs.get('email','')
        if Patient.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email in Use')})
        return super().validate(attrs)
