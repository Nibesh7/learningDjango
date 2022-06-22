
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp' #namespacing urls
urlpatterns = [
    path('', views.index),
    # path('products/', views.products,name='products'),
    # path('product-detail/<int:id>/', views.product_detail, name='product_detail'),
    # path('products/add', views.add_product, name='add_produt'),
    # path('products/update/<int:id>/', views.update_product, name='update_product'),
    # path('products/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('products/', views.ProductListView.as_view(),name='products'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/add', views.ProductCreateView.as_view(), name='add_produt'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='delete_product'),
    path('products/mylisting', views.my_listing,name='mylistings'),
   
]
