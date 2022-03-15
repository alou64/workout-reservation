from django.db import models
from datetime import date
# from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=60)
  class Meta:
    db_table = 'user'

class Appointment(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(default=date.today)
  slot_1 = models.PositiveSmallIntegerField(default=None)
  slot_2 = models.PositiveSmallIntegerField(default=None)
  status = models.CharField(max_length=30, default='upcoming')
  class Meta:
    db_table = 'appointment'





# class Timeslot(models.Model):
#   id = models.PositiveSmallIntegerField(primary_key=True)
#   date = models.DateField()
#   time = models.TimeField()
#   spots = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   class Meta:
#     db_table = 'timeslot'



# class Day(models.Model):
#   db_table = 'day'
#   id = models.PositiveSmallIntegerField(primary_key=True)
#   time_0 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_1 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_2 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_3 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_4 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_5 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_6 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_7 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_8 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
#   time_9 = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])



# class Appointment(models.Model):
#   db_table = 'appointment'
#   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#   date = models.ForeignKey(Day, on_delete=models.CASCADE)
#   start_time = models.CharField(max_length=10)
#   end_time = models.CharField(max_length=10)
