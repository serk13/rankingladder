from sqlalchemy.orm import sessionmaker
from .models import engine, Base, Player

# Initialisieren der Datenbank durch Erstellen aller Tabellen
def init_db():
    Base.metadata.create_all(engine)

# Hinzufügen eines neuen Spielers zur Datenbank
def add_player(name, score):
    session = Session()
    new_player = Player(name=name, score=score)
    session.add(new_player)
    session.commit()
    session.close()

# Abrufen aller Spieler, sortiert nach Punktzahl in absteigender Reihenfolge
def get_all_players():
    session = Session()
    players = session.query(Player).order_by(Player.score.desc()).all()
    session.close()
    return players

# Löschen eines Spielers anhand seiner ID
def delete_player(player_id):
    session = Session()
    player = session.query(Player).get(player_id)
    if player:
        session.delete(player)  # Der Spieler wird zur Löschung markiert
        session.commit()  # Die Änderungen werden in der Datenbank gespeichert
    session.close()  # Schließe die Sitzung



# Zurücksetzen der Punktzahlen aller Spieler
def reset_all_scores():
    session = Session()
    players = session.query(Player).all()
    for player in players:
        player.score = 0
    session.commit()
    session.close()

# Suchen von Spielern anhand ihres Namens (nicht case-sensitiv)
def search_player(name):
    session = Session()
    player = session.query(Player).filter(Player.name.ilike(f'%{name}%')).all()
    session.close()
    return player

# Aktualisieren der Punktzahl eines Spielers anhand seiner ID
def update_player_score(player_id, new_score):
    session = Session()
    player = session.query(Player).get(player_id)
    if player:
        player.score = new_score
        session.commit()
        session.close()
        return True
    session.close()
    return False

# Konfiguration des Session-Makers
Session = sessionmaker(bind=engine)
