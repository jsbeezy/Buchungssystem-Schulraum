from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    seats = models.IntegerField()
    hasBeamer = models.BooleanField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    fromTime = models.DateTimeField()
    toTime = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} bucht {self.room.name} von {self.fromTime} bis {self.toTime}"
