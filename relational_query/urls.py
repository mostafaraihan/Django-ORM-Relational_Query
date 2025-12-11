from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product_filter/', views.product_filter),
]