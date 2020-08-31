from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('', views.ProductList.as_view(), name='product'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/new/', views.ProducCreateView.as_view(), name='product-create'),
    path('<slug:slug>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('<slug:slug>/delete', views.ProductDeleteView.as_view(), name='product-delete'),
    # categories views goes here
    path('product/category/', views.CategoryList.as_view(), name='category'),
    path('product/<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),

]