from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class SchulraumAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Booking)
class BuchungAdmin(admin.ModelAdmin):
    list_display = ('fromTime', 'toTime', 'room')
