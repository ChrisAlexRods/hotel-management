from django.db import models

from django.db import models

class Booking(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    room_type = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
