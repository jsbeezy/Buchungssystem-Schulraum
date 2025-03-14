from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Room, Booking


class HomeView(TemplateView):
    template_name = "index.html"
    counter = 0
    grid_size = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_rooms = []
        rooms = Room.objects.all()
        room_positions = self.generate_room_positions()

        for room in rooms:
            if room.name in room_positions:
                position = room_positions[room.name]
                class_rooms.append({
                    "id": room.id,
                    "name": room.name,
                    "top": position["top"],
                    "left": position["left"]
                })

        context["class_rooms"] = class_rooms
        return context

    def generate_room_positions(self):
        room_positions = {}

        ring1_positions = self.create_ring_positions("1", 0, 0)
        room_positions.update(ring1_positions)

        ring2_positions = self.create_ring_positions("2", 0, self.grid_size + 2)
        room_positions.update(ring2_positions)

        hallway_length = 2
        for i in range(hallway_length):
            base_left = self.grid_size + i
            room_positions[f"N{i+1}"] = {"top": (self.grid_size // 2) - 1, "left": base_left}
            room_positions[f"S{i+1}"] = {"top": (self.grid_size // 2) + 1, "left": base_left}

        return room_positions

    def create_ring_positions(self, prefix, top_offset, left_offset):
        positions = {}
        ring_positions = []
        ring_positions.extend([(top_offset, left_offset + i) for i in range(self.grid_size)])
        ring_positions.extend([(top_offset + i, left_offset + self.grid_size - 1) for i in range(1, self.grid_size - 1)])
        ring_positions.extend([(top_offset + self.grid_size - 1, left_offset + i) for i in range(self.grid_size - 1, -1, -1)])
        ring_positions.extend([(top_offset + i, left_offset) for i in range(self.grid_size - 2, 0, -1)])

        for i, (top, left) in enumerate(ring_positions):
            class_room_number = i + 1
            class_room_id = f"{prefix}{class_room_number:02d}"
            if class_room_id in ["101", "105", "107", "109", "113", "201", "205", "209", "213", "215"]:
                continue
            positions[class_room_id] = {"top": top, "left": left}

        return positions

class ClassRoomAddBookingView(TemplateView):

    def get(self, request, id):
        context = {"class_room": Room.objects.get(id=id), "action": "ADD"}
        return render(request, 'class-room-add-booking.html', context)

class ClassRoomOptionsView(TemplateView):

    def get(self, request, id):
        context = {"class_room": Room.objects.get(id=id)}
        return render(request, 'class-room-option-select.html', context)

class ClassRoomBookingsView(TemplateView):

    def get(self, request, id):
        context = {"bookings": Booking.objects.filter(room_id=id)}
        return render(request, 'class-room-bookings.html', context)