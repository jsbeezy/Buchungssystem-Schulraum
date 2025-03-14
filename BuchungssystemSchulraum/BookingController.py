from datetime import datetime

from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse
from django.views.generic import TemplateView


class BookingsView(generic.TemplateView):
    template_name = "bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use data model instead
        context["bookings"] = [
            {"id": 0, "name": "Raum1", "from_time": datetime(2025, 1, 1), "to_time": datetime(2025, 12, 1)},
            {"id": 1, "name": "Raum2", "from_time": datetime(2025, 1, 5), "to_time": datetime(2025, 12, 5)}
        ]
        return context

class AddBookingView(TemplateView):
    def post(self, request, id, **kwargs):
        context = super().get_context_data(**kwargs)
        # context should return the model object of the provided id instead of this mock data
        context["booking"] = {"id": 0, "name": "Raum1", "from_time": datetime(2025, 1, 1), "to_time": datetime(2025, 12, 1)}
        return render(request, "add-booking-feedback.html", context)

class EditBookingView(View):
    def post(self, request, id):
        # to be implemented
        return JsonResponse("edit response")


class DeleteBookingView(View):
    def delete(self, request, id):
        # to be implemented
        return JsonResponse("delete response")