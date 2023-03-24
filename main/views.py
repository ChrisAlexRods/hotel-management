from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Event
from .serializers import BookingSerializer, EventSerializer

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
