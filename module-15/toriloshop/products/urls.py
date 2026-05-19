from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Product CRUD URLs
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    
    # Category CRUD URLs
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]