from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products),
    path('inner_join/', views.inner_join),
    path("outer_join/", views.outer_join),
]