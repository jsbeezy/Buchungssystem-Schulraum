# ReadMe

## Setup-Anleitung

### Voraussetzungen
- Python 3.x
- Django
- SQLite (oder ein anderes unterstütztes DBMS)

### Installation
1. Repository klonen:
   ```sh
   git clone <repository-url>
   cd buchungssystem-schulraum
   ```
2. Virtuelle Umgebung erstellen und aktivieren:
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Abhängigkeiten installieren:
   ```sh
   pip install -r requirements.txt
   ```
4. Datenbank migrieren:
   ```sh
   python manage.py migrate
   ```
5. Superuser erstellen (optional für Admin-Zugang):
   ```sh
   python manage.py createsuperuser
   ```
6. Server starten:
   ```sh
   python manage.py runserver
   ```

## Nutzerrollen

| Rolle     | Berechtigungen |
|-----------|----------------|
| **Schüler** | Räume suchen, eigene Buchungen verwalten |
| **Lehrer**  | Räume suchen, eigene Buchungen verwalten, Buchungen für Klassen vornehmen |
| **Admin**   | Räume verwalten, alle Buchungen einsehen und bearbeiten |

## Dummy-User
| Nutzername | Passwort | Rolle |
|------------|---------|-------|
| schueler1  | test123 | Schüler |
| lehrer1    | test123 | Lehrer |
| admin1     | admin123 | Admin |

Das System ist jetzt bereit zur Nutzung!

