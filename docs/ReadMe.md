# ReadMe

## Setup-Anleitung

### Voraussetzungen
- Python 3.x
- Pip

### Installation
1. Repository klonen:
   ```sh
   git clone https://github.com/jsbeezy/Buchungssystem-Schulraum.git
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
4. Datenbank migrieren (Hier werden auch die Daten für Räume und Testuser erstellt):
   ```sh
   python manage.py migrate
   ```
5. Server starten:
   ```sh
   python manage.py runserver
   ```

## Nutzerrollen

| Rolle     | Berechtigungen                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Schüler** | Kann den Raumplan sehen. Ansonsten machtlos.                                                                                      |
| **Lehrer**  | Kann den Raumplan sehen, Räume anhand von Sitzplätzen und Beamerbesitz suchen, Raumbuchungen einsehen, eigene Buchungen verwalten |
| **Admin**   | Alles, was der Lehrer kann, plus Zugriff auf die Adminoberfläche /admin zu Verwaltungszwecken                                     |

## Dummy-User
Die folgenden Benutzer werden automatisch während der Migration erstellt und stehen zum Testen der Anwendung zur Verfügung:

| Nutzername | Passwort | Rolle |
|------------|---------|-------|
| schüler    | 123     | Schüler |
| lehrer     | 123     | Lehrer |
| admin      | 123     | Admin |

Das System ist jetzt bereit zur Nutzung!


## Folgende Funktionalitäten bietet diese Anwendung:

- Login-Funktionalität
- Die oben erwähnten Berechtigungsstufen
- Schulraumübersicht
- Filter für die Schulraumübersicht, die bei der Suche nach Räumen mit mindestens X Sitzplätzen und Räumen mit Beamern helfen
- Raum Detailansicht, wo die Raumdaten angezeigt werden
- Buchungsübersicht für einen Raum inkl. Filter nach Datum
- Buchungserstellung für einen Raum
- Übersicht der eigenen, bestehenden Buchungen inkl. Filter nach Datum
- Verwaltung der eigenen Buchungen (Bearbeiten, Löschen)
- Validierung beim Erstellen und Bearbeiten von Buchungen, sodass es nicht zu Überschneidungen kommen kann


## Weiteres
- Eine Registrierung gibt es nicht. Die Erstellung der Nutzerkonten wird von der Schulverwaltung (Admin im Admininterface) übernommen
- Die Räume in unserer hypothetischen Schule sind fest, es lassen sich keine neuen Räume anlegen (technisch gesehen schon im Admininterface, allerdings geht unsere Implementierung von dieser festen Raumstruktur aus)