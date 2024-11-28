"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Player


# Fixture zur Einrichtung einer In-Memory-Datenbank für die Tests.
@pytest.fixture(scope="module")
def setup_database():
    # In-Memory SQLite-Datenbank erstellen.
    engine = create_engine('sqlite:///:memory:')
    session_actual = sessionmaker(bind=engine)
    # Datenbankschema erstellen (Tabellen generieren).
    Base.metadata.create_all(engine)
    session = session_actual()

    yield session

    # Datenbank schließen und Tabellen löschen.
    session.close()
    Base.metadata.drop_all(engine)


# Test für das Spieler-Datenmodell.
def test_player_model(setup_database):
    session = setup_database
    # Neuen Spieler erstellen.
    player = Player(name="John Doe", score=100)
    session.add(player)
    session.commit()

    # Spieler aus der Datenbank abfragen.
    fetched_player = session.query(Player).filter_by(name="John Doe").first()
    # Überprüfen, ob der Spieler existiert und die richtigen Werte hat.
    assert fetched_player is not None
    assert fetched_player.name == "John Doe"
    assert fetched_player.score == 100


# Test für die Vermeidung von Duplikaten bei Spielern.
def test_player_duplicate(setup_database):
    session = setup_database
    # Spieler erstellen und in die Datenbank einfügen.
    player = Player(name="Alice", score=200)
    session.add(player)
    session.commit()

    # Spieler mit dem Namen "Alice" abfragen.
    existing_player = session.query(Player).filter_by(name="Alice").first()
    # Überprüfen, ob der Spieler existiert.
    assert existing_player is not None
    players = session.query(Player).filter_by(name="Alice").all()
    # Sicherstellen, dass kein Duplikat existiert.
    assert len(players) == 1


# Test für die Aktualisierung der Punktzahl eines Spielers.
def test_player_score_update(setup_database):
    session = setup_database

    # Spieler abfragen, sicherstellen, dass er existiert oder ihn hinzufügen.
    player = session.query(Player).filter_by(name="John Doe").first()
    if player is None:
        # Spieler hinzufügen, wenn er nicht existiert.
        player = Player(name="John Doe", score=100)
        session.add(player)
        session.commit()

    # Aktualisiere die Punktzahl des Spielers.
    player.score = 150
    session.commit()

    # Abfrage: Aktualisierte Punktzahl überprüfen.
    updated_player = session.query(Player).filter_by(name="John Doe").first()
    assert updated_player.score == 150


# Test für das Löschen eines Spielers aus der Datenbank.
def test_player_deletion(setup_database):
    session = setup_database

    # Abfrage: Spieler "John Doe" aus der Datenbank abfragen.
    player = session.query(Player).filter_by(name="John Doe").first()

    # Falls der Spieler nicht existiert, füge ihn zur Datenbank hinzu.
    if player is None:
        player = Player(name="John Doe", score=100)
        session.add(player)
        session.commit()

    # Sicherstellen, dass der Spieler existiert, bevor er gelöscht wird.
    assert player is not None, "Player 'John Doe' does not exist in the database."

    # Spieler löschen.
    session.delete(player)
    session.commit()

    # Nach dem Spieler in der Datenbank suchen, um sicherzustellen, dass er gelöscht wurde.
    deleted_player = session.query(Player).filter_by(name="John Doe").first()

    # Überprüfen, ob der Spieler nach der Löschung nicht mehr existiert.
    assert deleted_player is None, "Player 'John Doe' was not deleted."
"""