from django.urls import path
from UserApp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('department/<item>/', views.department, name="department"),
    path('doctors/', views.doctors, name="doctors"),
    path('contact/', views.contact, name="contact"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('singledetails/<int:dataid>', views.singledetails, name="singledetails"),
    path('BookingSave/', views.BookingSave, name="BookingSave")
]
