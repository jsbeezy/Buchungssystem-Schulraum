from django.db import migrations

EXCLUDED_ROOMS = {
    '1': {'101', '105', '107', '109', '113'},
    '2': {'201', '205', '209', '213', '215'}
}

HALLWAY_ROOMS = ['N1', 'S1', 'N2', 'S2']


def generate_room_names():
    room_names = []
    for prefix in ['1', '2']:
        for room_num in range(1, 17):
            room_id = f"{prefix}{room_num:02d}"
            if room_id not in EXCLUDED_ROOMS[prefix]:
                room_names.append(room_id)
    room_names.extend(HALLWAY_ROOMS)
    return room_names


def add_rooms(apps, schema_editor):
    room = apps.get_model('BuchungssystemSchulraum', 'room')
    rooms = [room(name=name) for name in generate_room_names()]
    room.objects.using(schema_editor.connection.alias).bulk_create(rooms)


def remove_rooms(apps, schema_editor):
    room = apps.get_model('BuchungssystemSchulraum', 'room')
    room.objects.using(schema_editor.connection.alias).filter(
        name__in=generate_room_names()
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('BuchungssystemSchulraum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_rooms,
            reverse_code=remove_rooms,
            atomic=True
        ),
    ]