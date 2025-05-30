from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required(login_url='login_page')
def create_items(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity') 
        user = request.user
        Item.objects.create(name=name, description=description, price=price, quantity=quantity, user=user)
        return redirect('list_items')
    return render(request, 'items/create_items.html')


@login_required(login_url='login_page')
def list_items(request):
    unchecked_items = Item.objects.filter(user=request.user, checked=False)
    checked_items = Item.objects.filter(user=request.user, checked=True)
    return render(request, 'items/list_items.html', {
        "unchecked_items": unchecked_items,
        "checked_items": checked_items
    })

@login_required(login_url='login_page')
def update_items(request, id):
    item = Item.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')   
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')  
        item.name = name
        item.description = description
        item.price = price
        item.quantity = quantity  
        item.save()
        return redirect('list_items')
    return render(request, 'items/update_items.html', {"item": item})


@login_required(login_url='login_page')
def delete_items(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item.delete()
        return redirect('list_items')
    return render(request, 'items/delete_items.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        existing_user = authenticate(username=username, password=password)
        if existing_user is not None:
            login(request, existing_user)
            return redirect('list_items')
        else:
            messages.error(request, 'Invalid Username or Password', extra_tags='danger')
            return redirect('login_page')
    
    return render(request, 'accounts/login.html')

@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect('login_page')   

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        existing_user = User.objects.filter(username=username)

        if existing_user.exists():
            messages.error(request, 'Username already exists', extra_tags='danger')
            return redirect('sign_up')
        
        user = User.objects.create_user(first_name=first_name, username=username, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'User account created successfully', extra_tags='success')
        return redirect('sign_up')
    return render(request, 'accounts/signup.html')

@login_required(login_url='login_page')
@require_POST
def toggle_checked(request, id):
    item = Item.objects.get(id=id, user=request.user)
    item.checked = not item.checked
    item.save()
    return redirect('list_items')
