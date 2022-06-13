from django.http import HttpResponse
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

def add_product(request):
    if request.method =='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = Product(name=name,price=price,desc=desc,image=image)
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