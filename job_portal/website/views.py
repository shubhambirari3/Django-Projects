from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl
import os

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):
    return render(request, 'website/login.html')

def create_account(request):
    return render(request, 'website/create_account.html')

def job_application(request):
    if request.method == 'POST':
        # Handle form submission
        position = request.POST['position']
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['Gender']
        dob = request.POST['dob']
        contact = request.POST['contact']
        email = request.POST['email']
        location = request.POST['location']
        address = request.POST['adress']
        tech = request.POST['tech']
        skills = request.POST['skills']
        edu = request.POST['edu']
        uni = request.POST['uni']
        cgpa = request.POST['cgpa']
        passyear = request.POST['passyear']
        gap = request.POST['gap']
        fresher = request.POST['fresher']
        exp = request.POST['exp']
        current = request.POST['current']
        resume = request.FILES['resume']

        # Save resume to a specific folder
        resume_path = os.path.join('resumes', resume.name)
        with open(resume_path, 'wb+') as destination:
            for chunk in resume.chunks():
                destination.write(chunk)

        # Save data to Excel file
        excel_path = 'job_applications.xlsx'
        if not os.path.exists(excel_path):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(['Position', 'Name', 'Age', 'Gender', 'DOB', 'Contact', 'Email', 'Location', 'Address', 'Tech', 'Skills', 'Education', 'University', 'CGPA', 'Passing Year', 'Gap', 'Fresher', 'Experience', 'Current Company', 'Resume'])
        else:
            workbook = openpyxl.load_workbook(excel_path)
            sheet = workbook.active

        sheet.append([position, name, age, gender, dob, contact, email, location, address, tech, skills, edu, uni, cgpa, passyear, gap, fresher, exp, current, resume_path])
        workbook.save(excel_path)

        return HttpResponse("Form submitted successfully!")

    return render(request, 'website/sample_form.html')
