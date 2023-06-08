from django.db import models

class Contact(models.Model):
    Message = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Subject = models.CharField(max_length=20, null=True, blank=True)

class Booking(models.Model):
    Doctor = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)