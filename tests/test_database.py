import pytest
from src.database import (
    init_db, add_player, get_all_players, update_player_score, delete_player,
    reset_all_scores, search_player, Session
)
from src.models import Player


# Fixture zur Einrichtung der Testdatenbank
# REMINDER: Kein TestPy
@pytest.fixture(scope="module")
def test_db():
    # Initialisiere die Datenbank und füge Testdaten hinzu
    init_db()

    # Füge einen Spieler "Jane Doe" mit einer Punktzahl von 150 zur Datenbank hinzu
    add_player("Jane Doe", 150)

    # Liefere die Sitzung (Session) für die Tests zurück
    yield Session()

    # Bereinige die Datenbank nach den Tests (lösche alle Spieler)
    session = Session()
    session.query(Player).delete()
    session.commit()
    session.close()


# Test zum Hinzufügen eines Spielers
def test_add_player(test_db):
    session = Session()

    # Füge einen Spieler "Alice" mit einer Punktzahl von 200 hinzu
    add_player("Alice", 200)

    # Abfrage: Spieler "Alice" aus der Datenbank abfragen
    player = session.query(Player).filter_by(name="Alice").first()

    # Überprüfe, ob der Spieler erfolgreich hinzugefügt wurde
    assert player is not None
    assert player.score == 200

    session.close()


# Test zum Abrufen aller Spieler
def test_get_all_players(test_db):
    session = Session()

    # Füge einen Spieler "Bob" mit einer Punktzahl von 250 hinzu
    add_player("Bob", 250)

    # Abrufen aller Spieler aus der Datenbank
    players = get_all_players()

    # Überprüfen, ob mindestens 2 Spieler in der Datenbank vorhanden sind
    assert len(players) >= 2

    session.close()


# Test zur Aktualisierung der Punktzahl eines Spielers
def test_update_player_score(test_db):
    session = Session()

    # Abfrage: Spieler "Jane Doe" aus der Datenbank abfragen
    player = session.query(Player).filter_by(name="Jane Doe").first()

    if player:
        # Aktualisiere die Punktzahl des Spielers auf 180
        successful_update = update_player_score(player.id, 180)

        # Aktualisiere die Sitzung, um die Änderungen widerzuspiegeln
        session.refresh(player)

        # Überprüfe, ob das Update erfolgreich war
        assert successful_update
        assert player.score == 180

    session.close()


# Test zum Löschen eines Spielers
def test_delete_player(test_db):
    session = test_db  # Verwende die von der Fixture bereitgestellte Sitzung

    # Abfrage: Spieler "Jane Doe" aus der Datenbank abfragen
    player = session.query(Player).filter_by(name="Jane Doe").first()

    # Sicherstellen, dass der Spieler existiert, bevor er gelöscht wird
    assert player is not None

    # Spieler löschen
    delete_player(player.id)  # Verwende die delete_player Methode

    # Neue Abfrage, um sicherzustellen, dass der Spieler gelöscht wurde
    deleted_player = session.query(Player).filter_by(id=player.id).first()

    # Überprüfen, ob der Spieler nach dem Löschen nicht mehr existiert
    assert deleted_player is None  # Der Spieler sollte nach dem Löschen nicht mehr existieren


# Test zum Zurücksetzen aller Punktzahlen
def test_reset_all_scores(test_db):
    # Setze alle Punktzahlen in der Datenbank auf 0
    reset_all_scores()

    # Abrufen aller Spieler
    players = get_all_players()

    # Überprüfen, ob alle Spieler eine Punktzahl von 0 haben
    assert all(player.score == 0 for player in players)


# Test zur Suche eines Spielers
def test_search_player(test_db):
    # Füge den Spieler "Alice" mit einer Punktzahl von 100 hinzu, bevor du ihn suchst
    add_player("Alice", 100)

    # Suche nach dem Spieler "Alice" in der Datenbank
    players = search_player("Alice")

    # Überprüfe, ob der Spieler in der Datenbank gefunden wurde
    assert len(players) > 0
    assert any(player.name == "Alice" for player in players)
