from dataclasses import fields
from django.contrib import admin
from .resource import SalaryResources
from .models import SalaryModel
from import_export.admin import ImportExportModelAdmin

@admin.register(SalaryModel)
class SalaryAdmin(ImportExportModelAdmin):
    pass
