from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, AppointmentSerializer
from .models import User, Appointment

# Create your views here.
class UserView(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()

class AppointmentView(viewsets.ModelViewSet):
  serializer_class = AppointmentSerializer
  queryset = Appointment.objects.all()
