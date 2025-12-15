from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('serialdata', views.serialdata),
    path('inner_join/', views.inner_join),
    path("outer_join/", views.outer_join),
    path("select_data/", views.select_data),
    path("forenkey_lookup/", views.forenkey_lookup),
    path('row_sql/', views.row_sql),
]