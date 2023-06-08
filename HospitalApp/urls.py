from django.urls import path
from HospitalApp import views
urlpatterns = [
    path('adminindex/', views.adminindex, name="adminindex"),
    path('department_details/', views.department_details, name="department_details"),
    path('save_department_details/', views.save_department_details, name="save_department_details"),
    path('display_department_details/', views.display_department_details, name="display_department_details"),
    path('editdepartmentdetails/<int:dataid>', views.editdepartmentdetails, name="editdepartmentdetails"),
    path('deletedepartmentdetails/<int:dataid>', views.deletedepartmentdetails, name="deletedepartmentdetails"),
    path('update_department_details/<int:dataid>', views.update_department_details, name="update_department_details"),
    path('doctor_details/', views.doctor_details, name="doctor_details"),
    path('save_doctor_details/', views.save_doctor_details, name="save_doctor_details"),
    path('display_doctor_details/', views.display_doctor_details, name="display_doctor_details"),
    path('deletedoctordetails/<int:dataid>', views.deletedoctordetails, name="deletedoctordetails"),
    path('editdoctordetails/<int:dataid>', views.editdoctordetails, name="editdoctordetails"),
    path('update_doctors_details/<int:dataid>', views.update_doctors_details, name="update_doctors_details"),
    path('appointment_details/', views.appointment_details, name="appointment_details"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('contact_del/<int:dataid>', views.contact_del, name="contact_del"),
    path('bookin_del/<int:dataid>', views.bookin_del, name="bookin_del"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminloginfun/', views.adminloginfun, name="adminloginfun"),
    path('adminlogoutfun/', views.adminlogoutfun, name="adminlogoutfun")

]
