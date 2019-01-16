from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.


class Vivechak(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\d{10})$',
                                                                        message='Enter 10 digits number only.')])
    adharcard = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\d{12})$',
                                                                           message='Enter 12 digits number only.')])
    pancard = models.CharField(max_length=20, validators=[RegexValidator(regex='^(.{10})$',
                                                                         message='Length should be 10.')])

    def __str__(self):
        return self.name+'('+self.mobile+')'


class Report(models.Model):
    date = models.DateField(blank=False, null=True)
    dhara = models.CharField(max_length=100, blank=False, default="")
    crime_no = models.CharField(max_length=50, blank=False, default="")
    date_of_dakhila = models.DateField(blank=False, null=True)
    by = models.CharField(max_length=100, blank=False, default="")
    vivechak = models.ForeignKey(Vivechak, models.SET_NULL, blank=False, null=True)
    # vivechak = models.CharField(blank=False, max_length=100, default="")
    banam = models.CharField(max_length=100, blank=False, default="")
    place = models.CharField(max_length=100, blank=False, default="")
    product_name = models.CharField(max_length=100, blank=False, default="")
    product_description = models.CharField(max_length=500, blank=False, default="")
    rack_no = models.CharField(max_length=50, blank=False, default="")
    shelf_no = models.CharField(max_length=50, blank=False, default="")
    box_no = models.CharField(max_length=50, blank=False, default="")


class StockIn(models.Model):
    product_name = models.CharField(max_length=100, blank=False, default="")
    entry_date_and_time = models.DateTimeField(default=datetime.now)


class StockOut(models.Model):
    product_name = models.CharField(max_length=100, blank=False, default="")
    exit_date_and_time = models.DateTimeField(default=datetime.now)
