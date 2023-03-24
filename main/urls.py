from django.urls import path
from . import views

urlpatterns = [
    path('api/bookings/', views.BookingListCreate.as_view()),
    path('api/events/', views.EventListCreate.as_view()),
]
