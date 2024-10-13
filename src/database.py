from sqlalchemy.orm import sessionmaker
from src.models import engine, Base, Player


# Initialisieren der Datenbank durch Erstellen aller Tabellen
def init_db():
    # Erstellt alle Tabellen, die im Base-Objekt definiert sind, falls sie noch nicht existieren
    Base.metadata.create_all(engine)


# Hinzufügen eines neuen Spielers zur Datenbank
def add_player(name, score):
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Erstellt ein neues Spieler-Objekt mit dem angegebenen Namen und Punktzahl
    new_player = Player(name=name, score=score)
    # Fügt den neuen Spieler der Sitzung hinzu
    session.add(new_player)
    # Speichert die Änderungen in der Datenbank
    session.commit()
    # Schließt die Sitzung
    session.close()


# Abrufen aller Spieler, sortiert nach Punktzahl in absteigender Reihenfolge
def get_all_players():
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Abfrage: Alle Spieler nach Punktzahl absteigend sortiert abrufen
    players = session.query(Player).order_by(Player.score.desc()).all()
    # Schließt die Sitzung
    session.close()
    # Gibt die Liste der Spieler zurück
    return players


# Löschen eines Spielers anhand seiner ID
def delete_player(player_id):
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Sucht den Spieler mit der angegebenen ID
    player = session.query(Player).get(player_id)  # Spieler wird in der Datenbank gesucht
    if player:
        # Wenn der Spieler gefunden wurde, wird er zur Löschung markiert
        session.delete(player)
        # Speichert die Änderungen in der Datenbank
        session.commit()
        # Schließt die Sitzung
        session.close()
        # Gibt True zurück, um anzuzeigen, dass der Spieler erfolgreich gelöscht wurde
        return True
    else:
        # Schließt die Sitzung auch, wenn der Spieler nicht gefunden wurde
        session.close()
        # Gibt False zurück, um anzuzeigen, dass der Spieler nicht existiert
        return False


# Zurücksetzen der Punktzahlen aller Spieler
def reset_all_scores():
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Abfrage: Alle Spieler abrufen
    players = session.query(Player).all()
    # Setzt die Punktzahl jedes Spielers auf 0
    for player in players:
        player.score = 0
    # Speichert die Änderungen in der Datenbank
    session.commit()
    # Schließt die Sitzung
    session.close()


# Suchen von Spielern anhand ihres Namens (nicht case-sensitiv)
def search_player(name):
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Abfrage: Spieler suchen, deren Name die Suchanfrage enthält (Groß- und Kleinschreibung ignorieren)
    player = session.query(Player).filter(Player.name.ilike(f'%{name}%')).all()
    # Schließt die Sitzung
    session.close()
    # Gibt die Liste der gefundenen Spieler zurück
    return player


# Aktualisieren der Punktzahl eines Spielers anhand seiner ID
def update_player_score(player_id, new_score):
    # Erstellt eine neue Sitzung, um mit der Datenbank zu interagieren
    session = Session()
    # Sucht den Spieler mit der angegebenen ID
    player = session.query(Player).get(player_id)
    if player:
        # Wenn der Spieler gefunden wurde, wird die Punktzahl aktualisiert
        player.score = new_score
        # Speichert die Änderungen in der Datenbank
        session.commit()
        # Schließt die Sitzung
        session.close()
        # Gibt True zurück, um anzuzeigen, dass die Aktualisierung erfolgreich war
        return True
    # Schließt die Sitzung, wenn der Spieler nicht gefunden wurde
    session.close()
    # Gibt False zurück, um anzuzeigen, dass der Spieler nicht existiert
    return False


# Konfiguration des Session-Makers
# Erstellt eine Session-Klasse, die mit der Datenbank-Engine verbunden ist und verwendet werden kann, um Sitzungen zu erstellen
Session = sessionmaker(bind=engine)
