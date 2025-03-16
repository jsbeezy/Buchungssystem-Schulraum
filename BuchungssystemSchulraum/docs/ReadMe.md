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
4. Datenbank migrieren und Dummy-User erstellen:
   ```sh
   python manage.py migrate
   ```
5. Server starten:
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
Die folgenden Benutzer werden automatisch während der Migration erstellt:

| Nutzername | Passwort | Rolle |
|------------|---------|-------|
| schüler    | 123     | Schüler |
| lehrer     | 123     | Lehrer |
| admin      | 123     | Admin |

Das System ist jetzt bereit zur Nutzung!

