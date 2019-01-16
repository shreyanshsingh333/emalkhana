from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Vivechak, Report, StockIn, StockOut)
class ViewAdmin(admin.ModelAdmin):
    pass
