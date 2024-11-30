from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Departement)
class DepartementAdmin(ImportExportModelAdmin):
    list_display = ('name' , 'description')
    pass

@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'departement', 'email')
    pass

@admin.register(My_Educational)
class My_EducationalAdmin(ImportExportModelAdmin):
    list_display = ('doctor', 'degree', 'university')




