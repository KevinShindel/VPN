from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'company']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'quote']


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'resource', 'traffic']
