from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('addmaal', AddMaalView.as_view(), name='addmaal'),
    path('exportvivechak', export, name='exportvivechak'),
    path('importvivechak', import_vivechak, name='import_vivechak'),
]
