from dataclasses import field
from multiprocessing import context
from pyexpat import model
from re import template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
def index(request ):
    return HttpResponse("hello")

# def products(request):
#     products = Product.objects.all()
#     context ={
#         'products':products
#     }
#     return render(request,'myapp/index.html',context)

#Class based view for above products[ListView]
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'

# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     context ={
#         'product':product
#     }
#     return render(request,'myapp/detail.html',context)

#Class based view for above product_detail[DetailView]
class ProductDetailView(DetailView):
    model= Product
    template_name= 'myapp/detail.html'
    context_object_name='product'

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


# Class Based View  for createing product [CreateView]

class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']


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

# Class Based View  for Updating product [UpdateView]
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix= "_update_form"

def delete_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/products')
    context ={
        'product':product
    }
    return render(request,'myapp/deleteProduct.html',context)
# class based view for deleting the product [DeleteView]
class ProductDelete(DeleteView):
    model=Product
    success_url= reverse_lazy('myapp:products')
    #reverse_lazy resolves url name to actual url path 
def my_listing(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {'products':products}
    return render(request, 'myapp/mylisting.html',context)