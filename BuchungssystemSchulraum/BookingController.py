from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Booking
from .models import Room
from django.contrib.auth.models import User
from datetime import datetime

class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        context = {"bookings": bookings}

        # todo: hier template einfügen oder so? oder vlt lieber getAll und getById/getByName als Routen, die nur eine jsonResponse geben fürs FE
        return render(request, 'bookings.html', context)

class AddBookingView(View):
    def post(self, request):
        room_id = request.POST.get('room')
        user_id = request.POST.get('user')
        from_time = request.POST.get('fromTime')
        to_time = request.POST.get('toTime')

        room = get_object_or_404(Room, id=room_id)
        user = get_object_or_404(User, id=user_id)

        booking = Booking.objects.create(
            room=room,
            user=user,
            fromTime=datetime.strptime(from_time, '%Y-%m-%d %H:%M:%S'),
            toTime=datetime.strptime(to_time, '%Y-%m-%d %H:%M:%S')
        )

        return JsonResponse({"message": "Booking added", "id": booking.id})

class EditBookingView(View):
    def post(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        booking.fromTime = request.POST.get('fromTime', booking.fromTime)
        booking.toTime = request.POST.get('toTime', booking.toTime)
        booking.save()

        return JsonResponse({"message": "Booking updated", "id": booking.id})

class DeleteBookingView(View):
    def delete(self, request, id):
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        return JsonResponse({"message": "Booking deleted"})
