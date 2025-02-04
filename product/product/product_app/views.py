from django.shortcuts import render , redirect , get_object_or_404
from .models import *

# Create your views here.

def product_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')
        product.objects.create(name = name , description=description , price = price , created_at = created_at)
        
        return redirect('product_list')
    return render(request , 'product_app/product_create.html')

def product_list(request):
    products = product.objects.all()

    return render (request , 'product_app/product_list.html',{'products':products})

def product_delete(request, product_id):
    product_instance = get_object_or_404(product, id=product_id)
    if request.method == "POST":
        product_instance.delete()
        return redirect("product_list")
    return render(request, 'product_app/product_delete.html', {'products': product_instance})

def product_update(request ,product_id):
    product_instance = get_object_or_404(product, id=product_id)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        product.name = name
        product.description = description
        product.price = price
        product.save()

        return redirect("product_list")
    
    return render(request , 'product_app/product_update.html', {'product': product_instance})


