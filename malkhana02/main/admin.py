from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Vivechak, MaalModel)
class ViewAdmin(admin.ModelAdmin):
    pass
