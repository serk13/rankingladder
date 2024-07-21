import pytest
from src.models import Base, engine, Player
from src.database import init_db, add_player, get_all_players, update_player_score, Session


@pytest.fixture(scope="module")
def test_db():
    # Datenbank initialisieren und Tabellen erstellen
    init_db()
    # Testdaten hinzufügen
    add_player("Jane Doe", 150)
    yield
    # Bereinige die Datenbank nach den Tests
    session = Session()
    session.query(Player).delete()
    session.commit()
    session.close()

def test_add_player(test_db):
    session = Session()
    player = session.query(Player).filter_by(name="Jane Doe").first()
    assert player is not None
    assert player.score == 150
    session.close()


def test_get_all_players(test_db):
    session = Session()
    add_player("Alice", 200)
    players = get_all_players()
    assert len(players) == 2  # Einschließlich des aus test_add_player
    assert players[0].name == "Alice"
    assert players[0].score == 200
    session.close()

def test_update_player_score(test_db):
    session = Session()
    player = session.query(Player).filter_by(name="Jane Doe").first()
    if player:
        update_player_score(player.id, 180)
        session.refresh(player)  # Aktualisiere das Objekt mit neuen Daten aus der Datenbank
        assert player.score == 180
    else:
        assert False, "Player not found"  # Fügt eine aussagekräftigere Fehlermeldung hinzu
    session.close()

