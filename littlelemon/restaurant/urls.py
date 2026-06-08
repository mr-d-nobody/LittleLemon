
from django import views
from django.contrib import admin
from django.urls import path
from .views import index, sayHello

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.sayHello, name='hello'),
    
]