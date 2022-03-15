from django.contrib import admin
from .models import User, Appointment

class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email')

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ('id', 'user_id', 'date', 'slot_1', 'slot_2', 'status')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
