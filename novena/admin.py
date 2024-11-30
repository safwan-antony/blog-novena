from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Patient)
class PatientImportExport(ImportExportModelAdmin):
    list_display = ("first_name","last_name","email","gender")
    pass

@admin.register(Appoinment)
class AppoinmentImportExport(ImportExportModelAdmin):
    list_display = ("patient","day","time","status")
    pass

@admin.register(Contact)
class ContactImportExport(ImportExportModelAdmin):
    list_display = ("full_name","email","phone","subject")
    pass

@admin.register(Message)
class MessageImportExport(ImportExportModelAdmin):
    list_display = ("doctor","patient","created","updated")
    pass