from .models import Booking, Menu
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics, viewsets

from restaurant.serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def sayHello(request):
    return HttpResponse("Hello, welcome to Little Lemon!")


def index(request):
    return render(request, 'index.html', {})


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer