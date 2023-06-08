from django.db import models

class Department(models.Model):
    DepartmentName = models.CharField(max_length=100, null=True, blank=True)
    Image2 = models.ImageField(upload_to="Profile", null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)

class Doctors(models.Model):
    DoctorName = models.CharField(max_length=100, null=True, blank=True)
    DepartmentName = models.CharField(max_length=100, null=True, blank=True)
    Speciality = models.CharField(max_length=100, null=True, blank=True)
    About = models.CharField(max_length=1000, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile1", null=True, blank=True)
    Overview = models.CharField(max_length=1000, null=True, blank=True)
    Awards_Recognition = models.CharField(max_length=1000, null=True, blank=True)



