from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(DigitalProfile)
class DigitalProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'date']


@admin.register(PersonalDetail)
class DigitalProfileAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'name', 'mobile', 'location']
