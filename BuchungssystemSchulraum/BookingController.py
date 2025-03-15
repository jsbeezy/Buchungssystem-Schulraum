from django.contrib.auth.decorators import permission_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Booking
from .models import Room
from django.contrib.auth.models import User
from datetime import datetime, date

class BookingForUserView(View):
    def get(self, request):
        if not request.user.is_staff:
            return render(request, "no-permission.html")

        bookings = Booking.objects.filter(user = request.user)
        context = {"bookings": bookings}

        return render(request, 'bookings.html', context)

class AddBookingView(TemplateView):
    def post(self, request, id):
        if not request.user.is_staff:
            return render(request, "no-permission.html")
        from_time = request.POST.get('fromTime')
        to_time = request.POST.get('toTime')

        from_datetime, to_datetime = buildDatetime(from_time, to_time)

        room = get_object_or_404(Room, id=id)

        booking = Booking.objects.create(
            room=room,
            user=request.user,
            fromTime=from_datetime,
            toTime=to_datetime
        )

        context = {"booking": booking, "action": "ADD"}
        return render(request, "booking-feedback.html", context)

class ShowEditBookingView(TemplateView):
    def get(self, request, id):
        if not request.user.is_staff:
            return render(request, "no-permission.html")
        booking = get_object_or_404(Booking, id=id)

        context = {"booking": booking, "action": "EDIT", "class_room": booking.room}
        return render(request, "class-room-add-booking.html", context)

class EditBookingView(TemplateView):
    def post(self, request, id):
        if not request.user.is_staff:
            return render(request, "no-permission.html")
        booking = get_object_or_404(Booking, id=id)
        oldFromTime = booking.fromTime
        oldToTime = booking.toTime

        from_time = request.POST.get('fromTime')
        to_time = request.POST.get('toTime')

        from_datetime, to_datetime = buildDatetime(from_time, to_time)

        booking.fromTime = from_datetime
        booking.toTime = to_datetime
        booking.save()

        context = {"booking": booking, "action": "EDIT", "oldFromTime": oldFromTime, "oldToTime": oldToTime}
        return render(request, "booking-feedback.html", context)

class DeleteBookingView(TemplateView):
    def post(self, request, id):
        if not request.user.is_staff:
            return render(request, "no-permission.html")
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        context = {"booking": booking, "action": "DELETE"}
        return render(request, "booking-feedback.html", context)

def buildDatetime(from_time, to_time):
    today = date.today()

    from_time_parsed = datetime.strptime(from_time, '%H:%M').time()
    to_time_parsed = datetime.strptime(to_time, '%H:%M').time()

    from_datetime = datetime.combine(today, from_time_parsed)
    to_datetime = datetime.combine(today, to_time_parsed)
    return from_datetime, to_datetime