from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from BuchungssystemSchulraum.models import Room, Booking

def check_permission(request):
    if not request.user.is_staff:
        return render(request, "error-page.html",
                      {"error_message": "Du bist nicht zum Einsehen dieser Seite berechtigt."})
    return None

class AddBookingToClassroom(TemplateView):
    def get(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        context = {"class_room": get_object_or_404(Room, id=id), "action": "ADD", "today": datetime.today()}

        return render(request, 'class-room-add-booking.html', context)

class ClassRoomOptionsView(TemplateView):
    def get(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        context = {"class_room": get_object_or_404(Room, id=id)}

        return render(request, 'class-room-option-select.html', context)

class ClassRoomBookingsView(TemplateView):
    def get(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        bookings = Booking.objects.filter(room_id=id)
        context = {"bookings": bookings, "class_room": get_object_or_404(Room, id=id)}

        return render(request, 'class-room-bookings.html', context)

class BookingForUserView(View):
    def get(self, request):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        bookings = Booking.objects.filter(user=request.user)
        context = {"bookings": bookings}

        return render(request, 'bookings.html', context)

class AddBookingView(View):
    def post(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        to_time = request.POST.get('toTime')
        from_time = request.POST.get('fromTime')

        to_time_parsed = datetime.strptime(to_time, '%Y-%m-%dT%H:%M')
        from_time_parsed = datetime.strptime(from_time, '%Y-%m-%dT%H:%M')

        room = get_object_or_404(Room, id=id)

        # Überprüfung, ob bereits eine Buchung für den gewählten Zeitraum existiert
        conflicting_booking = Booking.objects.filter(
            room=room, fromTime__lt=to_time_parsed, toTime__gt=from_time_parsed
        ).exists()

        if conflicting_booking:
            return render(request, "error-page.html", {"error_message": "Dieser Raum ist bereits im angegebenen Zeitraum gebucht."})

        booking = Booking.objects.create(
            room=room, user=request.user, fromTime=from_time_parsed, toTime=to_time_parsed
        )

        context = {"booking": booking, "action": "ADD"}
        return render(request, "booking-feedback.html", context)

class ShowEditBookingView(TemplateView):
    def get(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        booking = get_object_or_404(Booking, id=id)
        context = {"booking": booking, "action": "EDIT", "class_room": booking.room}
        return render(request, "class-room-add-booking.html", context)

class EditBookingView(View):
    def post(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        from_time = request.POST.get('fromTime')
        to_time = request.POST.get('toTime')

        from_time_parsed = datetime.strptime(from_time, '%Y-%m-%dT%H:%M')
        to_time_parsed = datetime.strptime(to_time, '%Y-%m-%dT%H:%M')

        booking = get_object_or_404(Booking, id=id)

        # Überprüfung, ob schon eine Buchung für den gewählten Zeitraum existiert, die NICHT dieselbe Buchung ist
        conflicting_booking = Booking.objects.filter(
            room=booking.room, fromTime__lt=to_time_parsed, toTime__gt=from_time_parsed
        ).exclude(id=booking.id).exists()

        if conflicting_booking:
            return render(request, "error-page.html", {"error_message": "Dieser Raum ist bereits im angegebenen Zeitraum gebucht."})

        booking.fromTime = from_time_parsed
        booking.toTime = to_time_parsed
        booking.save()

        context = {"booking": booking, "action": "EDIT"}
        return render(request, "booking-feedback.html", context)

class DeleteBookingView(TemplateView):
    def post(self, request, id):
        failed_check_view = check_permission(request)
        if failed_check_view:
            return failed_check_view

        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        context = {"booking": booking, "action": "DELETE"}

        return render(request, "booking-feedback.html", context)
