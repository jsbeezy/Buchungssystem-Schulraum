from django.db import migrations

EXCLUDED_ROOMS = {
    '1': {'101', '105', '107', '109', '113'},
    '2': {'201', '205', '209', '213', '215'}
}

HALLWAY_ROOMS = ['N1', 'S1', 'N2', 'S2']


def generate_room_names():
    room_names = []

    # Generate ring rooms for both prefixes
    for prefix in ['1', '2']:
        for room_num in range(1, 17):  # 16 rooms per ring
            room_id = f"{prefix}{room_num:02d}"
            if room_id not in EXCLUDED_ROOMS[prefix]:
                room_names.append(room_id)

    # Add hallway rooms
    room_names.extend(HALLWAY_ROOMS)
    return room_names


def add_rooms(apps, schema_editor):
    Room = apps.get_model('BuchungssystemSchulraum', 'Room')
    rooms = [Room(name=name) for name in generate_room_names()]
    Room.objects.using(schema_editor.connection.alias).bulk_create(rooms)


def remove_rooms(apps, schema_editor):
    Room = apps.get_model('BuchungssystemSchulraum', 'Room')
    Room.objects.using(schema_editor.connection.alias).filter(
        name__in=generate_room_names()
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('BuchungssystemSchulraum', '0001_initial'),  # Previous migration
    ]

    operations = [
        migrations.RunPython(
            add_rooms,
            reverse_code=remove_rooms,
            atomic=True
        ),
    ]