from multiprocessing import context
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Product
def index(request ):
    return HttpResponse("hello")

def products(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'myapp/index.html',context)

def product_detail(request,id):
    product = Product.objects.get(id=id)
    context ={
        'product':product
    }
    return render(request,'myapp/detail.html',context)

@login_required
def add_product(request):
    if request.method =='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        product.save()
    return render(request,'myapp/addProduct.html')

def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products/')
    context ={
        'product':product
    }
    return render(request,'myapp/updateProduct.html',context)


def delete_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    context ={
        'product':product
    }
    return render(request,'myapp/deleteProduct.html',context)

def my_listing(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {'products':products}
    return render(request, 'myapp/mylisting.html',context)