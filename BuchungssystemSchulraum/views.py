from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse
class HomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grid_size = 5
        rooms = []

        def create_ring_rooms(prefix, top_offset, left_offset):
            ring_rooms = []
            positions = []
            positions.extend([(top_offset, left_offset + i) for i in range(grid_size)])
            positions.extend([(top_offset + i, left_offset + grid_size - 1) for i in range(1, grid_size - 1)])
            positions.extend([(top_offset + grid_size - 1, left_offset + i) for i in range(grid_size - 1, -1, -1)])
            positions.extend([(top_offset + i, left_offset) for i in range(grid_size - 2, 0, -1)])

            for i, (top, left) in enumerate(positions):
                room_number = i + 1
                room_name = f"{prefix}{room_number:02d}"
                if room_name in ["101", "105", "107", "109", "113", "201", "205", "209", "213", "215"]:
                    continue
                ring_rooms.append({"name": room_name, "top": top, "left": left})
            return ring_rooms

        rooms.extend(create_ring_rooms("1", 0, 0))
        rooms.extend(create_ring_rooms("2", 0, grid_size + 2))

        hallway_length = 2
        for i in range(hallway_length):
            base_left = grid_size + i
            rooms.extend([
                {"name": f"N{i+1}", "top": (grid_size//2)-1, "left": base_left},
                {"name": f"S{i+1}", "top": (grid_size//2)+1, "left": base_left},
            ])

        context["rooms"] = rooms
        return context

class ClassRoomBookView(View):
    def post(self, request, id):
        print(f"Booking room {id}")
        return HttpResponseRedirect(reverse('index'))