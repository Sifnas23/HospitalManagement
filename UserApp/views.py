from django.shortcuts import render, redirect
from HospitalApp.models import Department, Doctors
from UserApp.models import Contact, Booking

def index(request):
    data = Department.objects.all()
    return render(request, "index.html", {"data": data})

def about(request):
    data = Department.objects.all()
    return render(request, "About.html", {"data": data})

def department(request,item):
    data1 = Department.objects.filter(DepartmentName=item)
    data = Department.objects.all()
    return render(request, "Department.html", {"data": data, "data1": data1})

def doctors(request):
    data2 = Doctors.objects.filter()
    data = Department.objects.all()
    return render(request, "Doctors.html", {"data": data, "data2": data2})

def contact(request):
    data = Department.objects.all()
    return render(request, "ContactUs.html", {"data": data})
def contactsave(request):
    if request.method == "POST":
        mes = request.POST.get("message")
        nam = request.POST.get("name")
        email = request.POST.get("email")
        sub = request.POST.get("subject")
        obj = Contact(Message=mes, Name=nam, Email=email, Subject=sub)
        obj.save()
        return redirect(contact)

def BookingSave(request):
    if request.method == "POST":
        doc = request.POST.get("doctor")
        nam = request.POST.get("name")
        age = request.POST.get("age")
        num = request.POST.get("number")
        emi = request.POST.get("email")
        dat = request.POST.get("date")
        tim = request.POST.get("time")
        obj = Booking(Doctor=doc, Name=nam,Age=age,Number=num, Email=emi, Date=dat, Time=tim)
        obj.save()
        return redirect(index)

def singledetails(request, dataid):
    data = Department.objects.all()
    data1 = Doctors.objects.get(id=dataid)
    return render(request, "singledoctordetails.html", {"data": data, "data1": data1})





