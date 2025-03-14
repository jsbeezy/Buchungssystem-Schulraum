from datetime import datetime

from django.views import generic
from datetime import datetime
from django.views import generic
from .models import Room  # Import the Room model

class HomeView(generic.TemplateView):
    template_name = "index.html"
    grid_size = 5  # Remove the counter, as we'll use Room IDs

    def generate_ring_positions(self, top_offset, left_offset):
        """Generates grid positions for a ring based on top-left offset."""
        positions = []
        # Top row (left to right)
        positions.extend([(top_offset, left_offset + i) for i in range(self.grid_size)])
        # Right column (top to bottom, excluding corners)
        positions.extend([(top_offset + i, left_offset + self.grid_size - 1) for i in range(1, self.grid_size - 1)])
        # Bottom row (right to left)
        positions.extend([(top_offset + self.grid_size - 1, left_offset + i) for i in range(self.grid_size - 1, -1, -1)])
        # Left column (bottom to top, excluding corners)
        positions.extend([(top_offset + i, left_offset) for i in range(self.grid_size - 2, 0, -1)])
        return positions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_rooms = []

        # Fetch all rooms from the database
        rooms = Room.objects.all()
        EXCLUDED_ROOMS = {
            '1': {'101', '105', '107', '109', '113'},
            '2': {'201', '205', '209', '213', '215'}
        }
        HALLWAY_ROOMS = {'N1', 'S1', 'N2', 'S2'}

        # Categorize rooms
        ring1_rooms = []
        ring2_rooms = []
        hallway_rooms = []
        for room in rooms:
            name = room.name
            if name in HALLWAY_ROOMS:
                hallway_rooms.append(room)
            elif name.startswith('1') and len(name) == 3:
                if name not in EXCLUDED_ROOMS['1']:
                    ring1_rooms.append(room)
            elif name.startswith('2') and len(name) == 3:
                if name not in EXCLUDED_ROOMS['2']:
                    ring2_rooms.append(room)

        # Sort ring rooms by their numeric suffix
        ring1_rooms_sorted = sorted(ring1_rooms, key=lambda x: int(x.name[1:3]))
        ring2_rooms_sorted = sorted(ring2_rooms, key=lambda x: int(x.name[1:3]))

        # Assign positions to Ring 1 and Ring 2 rooms
        ring1_positions = self.generate_ring_positions(0, 0)
        for room, pos in zip(ring1_rooms_sorted, ring1_positions):
            class_rooms.append({
                "id": room.id,
                "name": room.name,
                "top": pos[0],
                "left": pos[1]
            })

        ring2_positions = self.generate_ring_positions(0, self.grid_size + 2)
        for room, pos in zip(ring2_rooms_sorted, ring2_positions):
            class_rooms.append({
                "id": room.id,
                "name": room.name,
                "top": pos[0],
                "left": pos[1]
            })

        # Assign positions to hallway rooms
        for room in hallway_rooms:
            num = int(room.name[1])
            base_left = self.grid_size + (num - 1)
            if room.name.startswith('N'):
                top = (self.grid_size // 2) - 1
            else:  # Starts with 'S'
                top = (self.grid_size // 2) + 1
            class_rooms.append({
                "id": room.id,
                "name": room.name,
                "top": top,
                "left": base_left
            })

        context["class_rooms"] = class_rooms
        return context

# ... (Keep other views unchanged)

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
    template_name = "class-room-bookings.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookings"] = [
            {"id": 0, "name": "Raum1", "from_time": datetime(2025, 1, 1), "to_time": datetime(2025, 12, 1)},
            {"id": 1, "name": "Raum2", "from_time": datetime(2025, 1, 5), "to_time": datetime(2025, 12, 5)}
        ]
        return context