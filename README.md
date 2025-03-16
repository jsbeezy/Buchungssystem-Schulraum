Virtual environment setup:

- make sure to have python and pip installed on your system
- run the following commands in the root directoy of the project

1:
python -m venv venv

2: 
venv\Scripts\activate

3:
pip install -r requirements.txt


And that's it! Now you should be able to run the project with:

python manage.py runserver




TO-DOs:
- beim Buchen von Räumen Error, wenn für den Timeslot schon eine Buchung vorhanden ist und entsprechend nicht persistieren
- Suchfunktion für Räume anhand von hasBeamer und seats properties (z.B.: hat der Raum einen Beamer? Hat er mindestens X Sitzplätze?)
- Serienbuchung (z.B. checkBox "Serienbuchung?" und falls angehakt -> Enddatum der Serienbuchung angeben, dann wird jede Woche zur selben Zeit gebucht)

Nice-to-have:
- bessere Übersicht in den Buchungsübersichten ("deine Buchungen" und Raumübersicht)
    -> evtl. in der Raumübersicht nach Tag filtern können
- bei "deine Buchungen" am besten Aufteilung nach Raum