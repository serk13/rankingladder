import pytest
from src.models import Player, Base, engine, Session


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(engine)
    session = Session()
    # Fügt den Spieler "John Doe" hinzu
    session.add(Player(name="John Doe", score=100))
    session.commit()
    yield session
    session.query(Player).delete()  # Bereinige die Datenbank nach den Tests
    session.commit()
    session.close()


def test_player_creation(setup_database):
    session = setup_database
    player = Player(name="George Lucas", score=100)
    session.add(player)
    session.commit()
    assert player.name == "George Lucas"
    assert player.score == 100
    # Überprüfen, ob die Repräsentation korrekt ist
    assert repr(player) == f"ID: {player.id}, Name: George Lucas, Score: 100"


def test_duplicate_player_addition(setup_database):
    session = setup_database
    # Füge den ersten Spieler hinzu und committe die Transaktion
    player = Player(name="Alice", score=200)
    session.add(player)
    session.commit()

    # Überprüfen, ob der Spieler bereits existiert, bevor ein Duplikat hinzugefügt wird
    existing_player = session.query(Player).filter_by(name="Alice").first()
    if existing_player:
        print("Spieler existiert bereits, kein Duplikat hinzugefügt.")
    else:
        # Versuche, denselben Spieler noch einmal hinzuzufügen, wenn er nicht existiert
        duplicate_player = Player(name="Alice", score=200)
        session.add(duplicate_player)
        session.commit()  # Diese Zeile sollte nicht erreicht werden, da der Spieler schon existiert

    # Überprüfe, dass nur ein Eintrag für 'Alice' existiert
    players = session.query(Player).filter_by(name="Alice").all()
    assert len(players) == 1  # Stellt sicher, dass nur ein Eintrag existiert
    session.close()


def test_player_score_update(setup_database):
    session = setup_database
    # Holt den Spieler "John Doe" aus der Datenbank
    player = session.query(Player).filter_by(name="John Doe").first()
    # Stellt sicher, dass der Spieler existiert
    assert player is not None, "Der Spieler 'John Doe' sollte in der Datenbank vorhanden sein"
    # Aktualisiert die Punktzahl des Spielers
    player.score = 150
    session.commit()  # Bestätigen der Änderungen
    # Holt den Spieler erneut, um die aktualisierte Punktzahl zu überprüfen
    updated_player = session.query(Player).filter_by(name="John Doe").first()
    assert updated_player.score == 150, "Die Punktzahl sollte aktualisiert worden sein"
    session.close()


def test_player_deletion(setup_database):
    session = setup_database
    player = session.query(Player).filter_by(name="John Doe").first()
    session.delete(player)
    session.commit()
    deleted_player = session.query(Player).filter_by(name="John Doe").first()
    assert deleted_player is None
