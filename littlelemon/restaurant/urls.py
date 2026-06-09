
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.sayHello, name='hello'),
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
]