from django.views import generic
class HomeView(generic.TemplateView):
    template_name = "index.html"
    counter = 0
    grid_size = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_rooms = []

        class_rooms.extend(self.create_ring_class_rooms("1", 0, 0))
        class_rooms.extend(self.create_ring_class_rooms("2", 0, self.grid_size + 2))

        hallway_length = 2
        for i in range(hallway_length):
            base_left = self.grid_size + i
            class_rooms.extend([
                {"id": self.counter, "name": f"N{i+1}", "top": (self.grid_size//2)-1, "left": base_left},
                {"id": self.counter, "name": f"S{i+1}", "top": (self.grid_size//2)+1, "left": base_left},
            ])

        context["class_rooms"] = class_rooms
        return context

    def create_ring_class_rooms(self, prefix, top_offset, left_offset):
        ring_rooms = []
        positions = []
        positions.extend([(top_offset, left_offset + i) for i in range(self.grid_size)])
        positions.extend([(top_offset + i, left_offset + self.grid_size - 1) for i in range(1, self.grid_size - 1)])
        positions.extend([(top_offset + self.grid_size - 1, left_offset + i) for i in range(self.grid_size - 1, -1, -1)])
        positions.extend([(top_offset + i, left_offset) for i in range(self.grid_size - 2, 0, -1)])

        for i, (top, left) in enumerate(positions):
            class_room_number = i + 1
            class_room_id = f"{prefix}{class_room_number:02d}"
            if class_room_id in ["101", "105", "107", "109", "113", "201", "205", "209", "213", "215"]:
                continue
            ring_rooms.append({"id": self.counter, "name": class_room_id, "top": top, "left": left})
            self.counter += 1
        return ring_rooms

class ClassRoomAddBookingView(generic.TemplateView):
    template_name = "class-room-add-booking.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        # use data model instead
        context["class_room"] = {"id": id, "name": "test"}
        return context

class ClassRoomOptionsView(generic.TemplateView):
    template_name = "class-room-option-select.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        # use data model instead
        context["booking"] = {"id": id}
        return context

class ClassRoomBookingsView(generic.TemplateView):
    render_template = "class-room-bookings.html"