from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Hotel, Room

from rest_framework import viewsets
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def room_list(request, hotel_id):
    rooms = Room.objects.filter(hotel_id=hotel_id)
    return render(request, 'room_list.html', {'rooms': rooms})

def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        room.free = False  # Изменение статуса номера на занятый
        room.save()
        return redirect('room_list', hotel_id=room.hotel.id)
    return render(request, 'book_room.html', {'room': room})


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
