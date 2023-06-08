from django.shortcuts import render, redirect
from HospitalApp.models import Department, Doctors
from UserApp.models import Contact, Booking
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def adminindex(request):
    return render(request, "AdminIndex.html")

def department_details(request):
    return render(request, "Department_Details.html")
def save_department_details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # img1 = request.FILES["image1"]
        img2 = request.FILES["image2"]
        desc = request.POST.get("description")
        obj = Department(DepartmentName=name, Image2=img2, Description=desc)
        obj.save()
        return redirect(department_details)
def display_department_details(request):
    data = Department.objects.all()
    return render(request, "Display_Department.html", {'data': data})
def editdepartmentdetails(request, dataid):
    data = Department.objects.get(id=dataid)
    print(data)
    return render(request, "Edit_Department.html", {'data': data})
def deletedepartmentdetails(request, dataid):
    data = Department.objects.filter(id=dataid)
    data.delete()
    return redirect(display_department_details)
def update_department_details(request, dataid):
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("description")
        # try:
        #     img1 = request.FILES["image1"]
        #     fs = FileSystemStorage()
        #     file1 = fs.save(img1.name, img1)
        # except MultiValueDictKeyError:
        #     file1 = Department.objects.get(id=dataid).Image1
        try:
            img2 = request.FILES["image2"]
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = Department.objects.get(id=dataid).Image2
        Department.objects.filter(id=dataid).update(DepartmentName=name, Image2=file2, Description=desc)
        return redirect(display_department_details)


def doctor_details(request):
    data = Department.objects.all()
    return render(request, "Doctor_details.html", {'data': data})
def save_doctor_details(request):
    if request.method == "POST":
        name1 = request.POST.get("name1")
        name2 = request.POST.get("name2")
        spec = request.POST.get("speciality")
        about = request.POST.get("about")
        img = request.FILES["image"]
        over = request.POST.get("overview")
        awre = request.POST.get("awards")
        obj = Doctors(DoctorName=name1, DepartmentName=name2, Speciality=spec, About=about, Image=img, Overview=over, Awards_Recognition=awre)
        obj.save()
        return redirect(doctor_details)
def display_doctor_details(request):
    data = Doctors.objects.all()
    return render(request, "Display_Doctor.html", {'data': data})
def editdoctordetails(request, dataid):
    data1 = Doctors.objects.get(id=dataid)
    data = Department.objects.all()
    return render(request, "Edit_Doctor.html", {'data1': data1, 'data': data})
def deletedoctordetails(request, dataid):
    data = Doctors.objects.filter(id=dataid)
    data.delete()
    return redirect(display_doctor_details)
def update_doctors_details(request, dataid):
    if request.method == "POST":
        name1 = request.POST.get("name1")
        name2 = request.POST.get("name2")
        spec = request.POST.get("speciality")
        about = request.POST.get("about")
        over = request.POST.get("overview")
        awre = request.POST.get("awards")
        try:
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Doctors.objects.get(id=dataid).Image
        Doctors.objects.filter(id=dataid).update(DoctorName=name1, DepartmentName=name2, Speciality=spec, About=about, Image=file, Overview=over, Awards_Recognition=awre)
        return redirect(display_doctor_details)

def appointment_details(request):
    data = Booking.objects.all()
    return render(request, "Appointment_details.html", {"data": data})

def contact_details(request):
    data = Contact.objects.all()
    return render(request, "Contact_Details.html", {"data": data})

def contact_del(request, dataid):
    data = Contact.objects.filter(id=dataid)
    data.delete()
    return redirect(contact_details)

def bookin_del(request, dataid):
    data = Booking.objects.filter(id=dataid)
    data.delete()
    return redirect(appointment_details)

def admin_login(request):
    return render(request, "Admin_Login.html")

def adminloginfun(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(adminindex)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)
def adminlogoutfun(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

