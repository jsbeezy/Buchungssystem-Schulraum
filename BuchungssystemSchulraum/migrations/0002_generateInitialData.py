from django.db import migrations
from django.contrib.auth.models import User
from BuchungssystemSchulraum.models import Room, Booking
from datetime import timedelta, datetime, timezone


def generate_initial_data(apps, schema_editor):

    # Testnutzer erstellen
    User.objects.create_user(username="schüler", password="123", is_staff=False, is_superuser=False,
                             last_login=datetime.now())
    staff_user = User.objects.create_user(username="lehrer", password="123", is_staff=True, is_superuser=False,
                                          last_login=datetime.now())
    superuser = User.objects.create_user(username="admin", password="123", is_staff=True, is_superuser=True,
                                         last_login=datetime.now())

    # Diese Raumdaten sind abgestimmt auf die feste "Raumstruktur" unserer hypothetischen Schule
    rooms_data = [
        {"name": "102", "seats": 25, "hasBeamer": False},
        {"name": "103", "seats": 30, "hasBeamer": False},
        {"name": "104", "seats": 35, "hasBeamer": True},
        {"name": "106", "seats": 15, "hasBeamer": True},
        {"name": "108", "seats": 10, "hasBeamer": False},
        {"name": "110", "seats": 27, "hasBeamer": True},
        {"name": "111", "seats": 20, "hasBeamer": False},
        {"name": "112", "seats": 18, "hasBeamer": True},
        {"name": "114", "seats": 18, "hasBeamer": False},
        {"name": "115", "seats": 12, "hasBeamer": True},
        {"name": "116", "seats": 20, "hasBeamer": True},
        {"name": "202", "seats": 30, "hasBeamer": False},
        {"name": "203", "seats": 25, "hasBeamer": True},
        {"name": "204", "seats": 25, "hasBeamer": False},
        {"name": "206", "seats": 28, "hasBeamer": False},
        {"name": "207", "seats": 25, "hasBeamer": True},
        {"name": "208", "seats": 18, "hasBeamer": False},
        {"name": "210", "seats": 20, "hasBeamer": False},
        {"name": "211", "seats": 12, "hasBeamer": False},
        {"name": "212", "seats": 32, "hasBeamer": True},
        {"name": "214", "seats": 30, "hasBeamer": False},
        {"name": "216", "seats": 26, "hasBeamer": True},
        {"name": "N1", "seats": 10, "hasBeamer": False},
        {"name": "N2", "seats": 10, "hasBeamer": True},
        {"name": "S1", "seats": 10, "hasBeamer": False},
        {"name": "S2", "seats": 10, "hasBeamer": True},
    ]

    for room_data in rooms_data:
        Room.objects.create(name=room_data["name"], seats=room_data["seats"], hasBeamer=room_data["hasBeamer"])

    rooms = Room.objects.all()

    # Beispielbuchungen für die Räume generieren
    for room in rooms:
        for i in range(3):
            from_time = datetime.now() + timedelta(days=i, hours=i)
            to_time = from_time + timedelta(hours=i * 2)

            Booking.objects.create(
                room=room,
                fromTime=from_time,
                toTime=to_time,
                user=staff_user if i % 2 == 0 else superuser
            )

class Migration(migrations.Migration):

    dependencies = [
        ('BuchungssystemSchulraum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_initial_data),
    ]
