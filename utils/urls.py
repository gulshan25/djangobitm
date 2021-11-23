from django.urls import path 
from . import views

urlpatterns = [
    path('sendemail/', views.sent_mail,name='sendemail'),
]