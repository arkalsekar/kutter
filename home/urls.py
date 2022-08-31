from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path('urls', views.ViewUrls, name="ViewUrls"),
    path("r/<slug>", views.Main_Redirect, name="Main_Redirect"),
]
