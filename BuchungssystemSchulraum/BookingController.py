from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Booking
from .models import Room
from django.contrib.auth.models import User
from datetime import datetime, date


class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        context = {"bookings": bookings}
        return render(request, 'bookings.html', context)

class AddBookingView(TemplateView):
    def post(self, request, id):
        room_id = request.POST.get('room')
        # uncomment once users are available
        # user_id = request.POST.get('user')
        user_id = User.objects.get(id=1).id

        from_time = request.POST.get('fromTime')
        to_time = request.POST.get('toTime')

        from_datetime, to_datetime = buildDatetime(from_time, to_time)

        room = get_object_or_404(Room, id=room_id)
        user = get_object_or_404(User, id=user_id)

        booking = Booking.objects.create(
            room=room,
            user=user,
            fromTime=from_datetime,
            toTime=to_datetime
        )

        context = {"booking": booking, "action": "ADD"}
        return render(request, "booking-feedback.html", context)

class ShowEditBookingView(TemplateView):
    def get(self, request, id):
        booking = get_object_or_404(Booking, id=id)

        context = {"booking": booking, "action": "EDIT"}
        return render(request, "class-room-add-booking.html", context)

class EditBookingView(TemplateView):
    def post(self, request, id):
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