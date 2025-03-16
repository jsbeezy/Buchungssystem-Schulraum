from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from BuchungssystemSchulraum.models import Room

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    grid_size = 5
    login_url = "/login/"

    # Generiert die äußerden Ringe aus Räumen für die Gebäudeübersicht
    def generate_room_positions(self):
        room_positions = {}

        ring1_positions = self.create_ring_positions("1", 0, 0)
        room_positions.update(ring1_positions)

        ring2_positions = self.create_ring_positions("2", 0, self.grid_size + 2)
        room_positions.update(ring2_positions)

        hallway_length = 2
        for i in range(hallway_length):
            base_left = self.grid_size + i
            room_positions[f"N{i + 1}"] = {"top": (self.grid_size // 2) - 1, "left": base_left}
            room_positions[f"S{i + 1}"] = {"top": (self.grid_size // 2) + 1, "left": base_left}

        return room_positions

    def create_ring_positions(self, prefix, top_offset, left_offset):
        positions = {}
        ring_positions = []
        ring_positions.extend([(top_offset, left_offset + i) for i in range(self.grid_size)])
        ring_positions.extend(
            [(top_offset + i, left_offset + self.grid_size - 1) for i in range(1, self.grid_size - 1)])
        ring_positions.extend(
            [(top_offset + self.grid_size - 1, left_offset + i) for i in range(self.grid_size - 1, -1, -1)])
        ring_positions.extend([(top_offset + i, left_offset) for i in range(self.grid_size - 2, 0, -1)])

        for i, (top, left) in enumerate(ring_positions):
            class_room_number = i + 1
            class_room_id = f"{prefix}{class_room_number:02d}"
            if class_room_id in ["101", "105", "107", "109", "113", "201", "205", "209", "213", "215"]:
                continue
            positions[class_room_id] = {"top": top, "left": left}

        return positions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_rooms = []
        rooms = Room.objects.all()

        # Anfrage-Parameter holen
        seats = self.request.GET.get("seats")
        has_beamer = self.request.GET.get("hasBeamer") == "true" if "hasBeamer" in self.request.GET else None

        # Positionen für alle Räume generieren
        room_positions = self.generate_room_positions()

        for room in rooms:
            if room.name in room_positions:
                position = room_positions[room.name]

                # Prüfen, ob der Raum die Suchkriterien erfüllt
                matches = True
                if seats and room.seats < int(seats):
                    matches = False
                if has_beamer is not None and room.hasBeamer != has_beamer:
                    matches = False

                class_rooms.append({
                    "id": room.id,
                    "name": room.name,
                    "top": position["top"],
                    "left": position["left"],
                    "matches": matches,  # True = normal klickbar, False = ausgegraut
                })

        context["class_rooms"] = class_rooms
        return context