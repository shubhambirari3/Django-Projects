from django.shortcuts import render ,redirect , get_object_or_404
from .models import contactM

# Create your views here.


def message_list(request):
    messages = contactM.objects.all().order_by('-created_at')     #see here maybe error
    return render(request , 'contact_us_app/message_list.html' , {'messages':messages})

def message_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactM.objects.create(name=name , email=email , message=message)
        return redirect('message_list')
    return render(request , 'contact_us_app/message_create.html')

def message_details(request , contact_id):
    message = get_object_or_404(contactM , id=contact_id)
    return render(request , 'contact_us_app/message_details.html' , {'message':message})


def message_delete(request , contact_id):
    message = get_object_or_404(contactM , id = contact_id)
    if request.method == "POST":
        message.delete()
        return redirect('message_list')
    return render(request ,'contact_us_app/message_delete.html' , {'contactM': message})



