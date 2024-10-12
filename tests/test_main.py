import pytest
from unittest.mock import patch
from src.main import main
from src.models import Player, Session
from src.database import init_db, add_player

# Fixture zur Einrichtung der Datenbank für Tests
@pytest.fixture(scope="module")
def setup_database():
    # Datenbank initialisieren und Tabellen erstellen
    init_db()
    # Beispiel-Daten hinzufügen: Füge einen Testspieler zur Datenbank hinzu
    add_player("Test Player", 100)
    yield
    # Bereinige die Datenbank nach den Tests, indem alle Spieler entfernt werden
    session = Session()
    session.query(Player).delete()
    session.commit()
    session.close()

# Test für das Beenden der Anwendung durch Benutzereingabe
# Erwartet, dass das Programm mit einer SystemExit-Ausnahme beendet wird
def test_main_exit():
    # Simuliert die Eingabe '7', was zum Beenden der Anwendung führen sollte
    with patch('builtins.input', return_value='7'):
        with pytest.raises(SystemExit):
            main()

# Test für die Benutzerinteraktion zum Hinzufügen eines neuen Spielers
def test_add_player_interaction():
    # Simuliert Benutzerinteraktionen: Auswahl '1' (Spieler hinzufügen), 'New Player', '120' (Punkte), '7' (Beenden)
    with patch('builtins.input', side_effect=['1', 'New Player', '120', '7']), \
         patch('builtins.print') as mocked_print:
        # Erwartet, dass das Programm mit einer SystemExit-Ausnahme endet
        with pytest.raises(SystemExit):
            main()
        # Überprüft, ob die erwartete Erfolgsmeldung ausgegeben wurde
        mocked_print.assert_any_call("Spieler New Player mit der Punktzahl 120 wurde hinzugefügt.")

# Test, der eine ungültige Menüoption simuliert und sicherstellt, dass die richtige Fehlermeldung ausgegeben wird
def test_invalid_option():
    # Simuliert ungültige Eingabe '8' und anschließend '7', um das Programm zu beenden
    with patch('builtins.input', side_effect=['8', '7']), \
         patch('builtins.print') as mocked_print:
        try:
            # Führt die Hauptfunktion der Anwendung aus
            main()
        except SystemExit:
            pass  # Ignoriere SystemExit, um den Rest des Tests fortzusetzen

        # Überprüft, ob die Fehlermeldung für die ungültige Auswahl ausgegeben wurde
        print_calls = [call.args[0].strip() for call in mocked_print.call_args_list]
        assert "Ungültige Auswahl. Bitte wähle eine gültige Option." in print_calls, f"Print calls: {print_calls}"