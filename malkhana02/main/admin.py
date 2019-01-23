from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(MaalModel)
class ViewAdmin(admin.ModelAdmin):
    pass


@admin.register(Vivechak)
class VivechakAdmin(ImportExportModelAdmin):
    pass
