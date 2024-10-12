import pytest
from unittest.mock import patch
from src.main import main
from src.models import Player, Session
from src.database import init_db, add_player


@pytest.fixture(scope="module")
def setup_database():
    # Datenbank initialisieren und Tabellen erstellen
    init_db()
    # Füge Beispiel-Daten hinzu
    add_player("Test Player", 100)
    yield
    # Bereinige die Datenbank nach den Tests
    session = Session()
    session.query(Player).delete()
    session.commit()
    session.close()


def test_main_exit():
    with patch('builtins.input', return_value='7'):
        with pytest.raises(SystemExit):
            main()


def test_add_player_interaction():
    # Simuliere Benutzerinteraktionen für das Hinzufügen eines neuen Spielers
    with patch('builtins.input', side_effect=['1', 'New Player', '120', '7']), \
            patch('builtins.print') as mocked_print:
        # Erwartet, dass das Programm mit einer SystemExit-Ausnahme endet
        with pytest.raises(SystemExit):
            main()
        # Überprüft, ob die erwartete Nachricht ausgegeben wurde
        mocked_print.assert_any_call("Spieler New Player mit der Punktzahl 120 wurde hinzugefügt.")


def test_invalid_option():
    # Test, der eine ungültige Menüauswahl behandelt
    with patch('builtins.input', side_effect=['8', '7']), \
         patch('builtins.print') as mocked_print:

        try:
            main()  # Führe das Programm aus
        except SystemExit:
            pass  # Ignoriere SystemExit, um den Rest des Tests fortzusetzen

        # Überprüft, ob die erwartete Nachricht ausgegeben wurde
        # Verwendet `call_args_list` und `strip()` zur Überprüfung
        print_calls = [call.args[0].strip() for call in mocked_print.call_args_list]
        assert "Ungültige Auswahl. Bitte wähle eine gültige Option." in print_calls, f"Print calls: {print_calls}"