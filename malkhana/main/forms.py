from django import forms
from .models import *


class VivechakForm(forms.ModelForm):
    class Meta:
        model = Vivechak
        fields = ['name', 'address', 'mobile', 'adharcard', 'pancard']

    def __init__(self, *args, **kwargs):
        super(VivechakForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['mobile'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['adharcard'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['pancard'].widget = forms.TextInput(attrs={'class': 'form-control'})


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class StockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = ['product_name']


class StockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = ['product_name']
