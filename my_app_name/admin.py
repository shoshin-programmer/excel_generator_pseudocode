from django.contrib import admin
from .models import HRBP 

# Register your models here.


@admin.register(HRBP)
class <ur name here>Admin(admin.ModelAdmin):
    list_display = ('date_uploaded', 'month', 'excel_reference')