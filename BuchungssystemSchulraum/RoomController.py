from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Room, Booking
from django.contrib.auth.hashers import make_password
from datetime import datetime

class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()

        # todo: hier template einfügen oder so? oder vlt lieber getAll und getById/getByName als Routen, die nur eine jsonResponse geben fürs FE
        return render(request, 'rooms.html', {"rooms": rooms})

class AddRoomView(View):
    def post(self, request):
        name = request.POST.get('name')
        room = Room.objects.create(name=name)

        return JsonResponse({"message": "Room added", "id": room.id})

class EditRoomView(View):
    def post(self, request, id):
        room = get_object_or_404(Room, id=id)
        room.name = request.POST.get('name', room.name)
        room.save()

        return JsonResponse({"message": "Room updated", "id": room.id})

class DeleteRoomView(View):
    def delete(self, request, id):
        room = get_object_or_404(Room, id=id)
        room.delete()

        return JsonResponse({"message": "Room deleted"})