from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Booking
from .models import Room
from django.contrib.auth.models import User
from datetime import datetime

class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        context = {"bookings": bookings}
        return render(request, 'bookings.html', context)

class AddBookingView(TemplateView):
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

        context = {"booking": booking, "action": "ADD"}
        return render(request, "booking-feedback.html", context)

class EditBookingView(TemplateView):
    def post(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        booking.fromTime = request.POST.get('fromTime', booking.fromTime)
        booking.toTime = request.POST.get('toTime', booking.toTime)
        booking.save()

        context = {"booking": booking, "action": "EDIT"}
        return render(request, "booking-feedback.html", context)

class DeleteBookingView(TemplateView):
    def delete(self, request, id):
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        context = {"booking": booking, "action": "DELETE"}
        return render(request, "booking-feedback.html", context)
