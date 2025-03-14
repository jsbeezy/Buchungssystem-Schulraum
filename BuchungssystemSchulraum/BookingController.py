from datetime import datetime

from django.views import generic, View
from django.http import JsonResponse

class BookingsView(generic.TemplateView):
    template_name = "bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use data model instead
        context["bookings"] = [
            {"id": 0, "name": "Raum1", "fromTime": datetime(2025, 1, 1), "toTime": datetime(2025, 12, 1)},
            {"id": 1, "name": "Raum2", "fromTime": datetime(2025, 1, 5), "toTime": datetime(2025, 12, 5)}
        ]
        return context

class AddBookingView(View):
    def post(self, request, id):
        # to be implemented
        return JsonResponse("add response")

class EditBookingView(View):
    def post(self, request, id):
        # to be implemented
        return JsonResponse("edit response")


class DeleteBookingView(View):
    def delete(self, request, id):
        # to be implemented
        return JsonResponse("delete response")