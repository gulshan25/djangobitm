from django.urls import path 
from . import views

urlpatterns = [
    path('sendemail/', views.sent_mail,name='sendemail'),
    path('exportcsv/', views.export_csv,name='exportcsv'),
]