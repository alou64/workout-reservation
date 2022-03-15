# convert model instances to JSON so frontend can work with the received data

from rest_framework import serializers
from .models import User, Appointment

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'email')

class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Appointment
    fields = ('id', 'user_id', 'date', 'slot_1', 'slot_2', 'status')
