import pytest
from src.database import init_db, add_player, get_all_players, update_player_score, delete_player, reset_all_scores, \
    search_player, Session
from src.models import Player


@pytest.fixture(scope="module")
def test_db():
    # ACHTUNG KEIN TEST: Pytest versucht , sie als Test zu finden und auszuführen, scheitert aber daran, weil sie als
    # Fixture und nicht als Testfunktion konzipiert ist. Datenbank initialisieren und Tabellen erstellen
    init_db()
    # Testdaten hinzufügen
    add_player("Jane Doe", 150)
    yield Session()  # Gibt die Session zurück für die Verwendung in Tests
    # Bereinige die Datenbank nach den Tests
    session = Session()
    session.query(Player).delete()
    session.commit()
    session.close()


def test_add_player(test_db):
    session = Session()
    # Füge einen weiteren Spieler hinzu und prüfe, ob die Daten korrekt sind
    add_player("Alice", 200)
    player = session.query(Player).filter_by(name="Alice").first()
    assert player is not None
    assert player.score == 200
    session.close()


def test_get_all_players(test_db):
    session = Session()
    add_player("Alice", 200)
    # Überprüfe, ob die Anzahl der Spieler in der Datenbank korrekt ist
    players = get_all_players()
    assert len(players) >= 2  # Muss mindestens 2 Spieler geben, die eingefügt wurden
    session.close()


def test_update_player_score(test_db):
    session = Session()
    # Aktualisiere die Punktzahl für einen bestehenden Spieler und prüfe das Ergebnis
    player = session.query(Player).filter_by(name="Jane Doe").first()
    if player:
        successful_update = update_player_score(player.id, 180)
        session.refresh(player)  # Aktualisiere das Objekt mit neuen Daten aus der Datenbank
        assert successful_update
        assert player.score == 180
    else:
        assert False, "Player not found"  # Fügt eine aussagekräftigere Fehlermeldung hinzu
    session.close()


def test_delete_player(test_db):
    session = Session()
    # Lösche einen Spieler und prüfe, ob er nicht mehr existiert
    player = session.query(Player).filter_by(name="Jane Doe").first()
    delete_player(player.id)
    player = session.query(Player).filter_by(name="Jane Doe").first()
    assert player is None
    session.close()


def test_reset_all_scores(test_db):
    session = Session()
    # Setze alle Punktzahlen zurück und prüfe, ob alle Punktzahlen 0 sind
    reset_all_scores()
    players = session.query(Player).all()
    all_scores_reset = all(p.score == 0 for p in players)
    assert all_scores_reset
    session.close()


def test_search_player(test_db):
    session = Session()
    # Suche nach einem Spieler und prüfe, ob die Rückgabe erwartungsgemäß erfolgt
    results = search_player("Jane")
    assert len(results) > 0  # Sollte mindestens einen Treffer geben, da "Jane Doe" vorhanden ist
    session.close()
