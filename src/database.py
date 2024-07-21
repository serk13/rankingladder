# Importieren der benötigten Module und Klassen für die Datenbankinteraktion.
from sqlalchemy.orm import sessionmaker
from .models import engine, Base, Player

# Funktion zum Initialisieren der Datenbank, d.h. zum Erstellen aller Tabellen, basierend auf den in models.py definierten Modellen.
def init_db():
    Base.metadata.create_all(engine)  # Erstellt alle Tabellen im Datenbankschema, falls sie noch nicht existieren.

# Funktion zum Hinzufügen eines neuen Spielers zur Datenbank.
def add_player(name, score):
    session = Session()  # Eine neue Session wird gestartet.
    new_player = Player(name=name, score=score)  # Erzeugen eines neuen Player-Objekts.
    session.add(new_player)  # Das neue Player-Objekt wird zur Session hinzugefügt.
    session.commit()  # Die Änderungen werden in der Datenbank festgeschrieben.
    session.close()  # Die Session wird geschlossen.

# Funktion, die alle Spieler aus der Datenbank abruft, sortiert nach ihrer Punktzahl in absteigender Reihenfolge.
def get_all_players():
    session = Session()  # Eine neue Session wird gestartet.
    players = session.query(Player).order_by(Player.score.desc()).all()  # Abfrage aller Spieler, sortiert nach Score.
    session.close()  # Die Session wird geschlossen.
    return players  # Rückgabe der Spielerliste.

# Funktion zum Löschen eines Spielers anhand seiner ID.
def delete_player(player_id):
    session = Session()  # Eine neue Session wird gestartet.
    player = session.query(Player).get(player_id)  # Versuch, den Spieler mit der gegebenen ID zu finden.
    if player:
        session.delete(player)  # Wenn der Spieler gefunden wurde, wird er aus der Datenbank gelöscht.
        session.commit()  # Die Änderungen werden in der Datenbank festgeschrieben.
    session.close()  # Die Session wird geschlossen.

# Funktion zum Zurücksetzen der Punkte aller Spieler in der Datenbank.
def reset_all_scores():
    session = Session()  # Eine neue Session wird gestartet.
    players = session.query(Player).all()  # Abfrage aller Spieler.
    for player in players:
        player.score = 0  # Setzen der Punktzahl jedes Spielers auf 0.
    session.commit()  # Die Änderungen werden in der Datenbank festgeschrieben.
    session.close()  # Die Session wird geschlossen.

# Funktion zur Suche nach Spielern anhand ihres Namens. Die Suche ist nicht case-sensitive.
def search_player(name):
    session = Session()  # Eine neue Session wird gestartet.
    player = session.query(Player).filter(Player.name.ilike(f'%{name}%')).all()  # Abfrage der Spieler, deren Namen den Suchbegriff enthalten.
    session.close()  # Die Session wird geschlossen.
    return player  # Rückgabe der gefundenen Spieler.

# Funktion zum Aktualisieren der Punktzahl eines Spielers anhand seiner ID.
def update_player_score(player_id, new_score):
    session = Session()  # Eine neue Session wird gestartet.
    player = session.query(Player).get(player_id)  # Versuch, den Spieler mit der gegebenen ID zu finden.
    if player:
        player.score = new_score  # Wenn der Spieler gefunden wurde, wird seine Punktzahl aktualisiert.
        session.commit()  # Die Änderungen werden in der Datenbank festgeschrieben.
        session.close()  # Die Session wird geschlossen.
        return True  # Rückgabe von True, wenn die Aktualisierung erfolgreich war.
    session.close()  # Die Session wird geschlossen, auch wenn der Spieler nicht gefunden wurde.
    return False  # Rückgabe von False, wenn kein Spieler gefunden wurde.

# Konfiguration der Session-Fabrik, die mit dem oben definierten Engine-Objekt verbunden ist.
Session = sessionmaker(bind=engine)
