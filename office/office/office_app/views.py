from django.shortcuts import render ,redirect ,get_object_or_404
from .models import *

# Create your views here.

def create_office(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        employees_count = request.POST.get('employees_count')
        created_at = request.POST.get('created_at')
        office.objects.create(name = name , location = location , employees_count  = employees_count , created_at = created_at )

        return redirect("list_office")
    
    return render(request , 'office_app/create_office.html')

def list_office(request):
    office_records = office.objects.all()

    return render(request , 'office_app/list_office.html' , {'records':office_records})

def delete_office(request , record_id):
    office_records = get_object_or_404(office , id = record_id)
    if request.method == "POST":
        office_records.delete()
        return redirect("list_office")
    
    return render(request , 'office_app/delete_office.html' , {'records':office_records})






