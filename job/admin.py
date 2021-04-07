from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(JobRecruiter)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_title', 'company_name', 'your_name', 'approved', 'date']


@admin.register(JobSeeker)
class UserJob(admin.ModelAdmin):
    list_display = ['id', 'user', 'job', 'date', 'saved', 'applied']
