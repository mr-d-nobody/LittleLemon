from .models import Booking, Menu
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics, viewsets

from restaurant.serializers import BookingSerializer, MenuSerializer


# Create your views here.
def sayHello(request):
    return HttpResponse("Hello, welcome to Little Lemon!")


def index(request):
    return render(request, 'index.html', {})


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer