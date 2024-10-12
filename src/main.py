# Import der benötigten Funktionen aus der database.py Datei für die Interaktion mit der Datenbank.
import sys
from src.database import init_db, add_player, get_all_players, update_player_score, delete_player, reset_all_scores, search_player

# Hilfsfunktion zur sicheren Abfrage von ganzzahligen Eingaben.
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)  # Benutzereingabe wird abgefragt.
        try:
            return int(user_input)  # Versucht die Eingabe in eine Ganzzahl umzuwandeln.
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")  # Fehlermeldung bei ungültiger Eingabe.

# Hauptfunktion des Programms, die das Menü steuert und auf Benutzereingaben reagiert.
def main():
    init_db()  # Initialisiert die Datenbank, indem die notwendigen Tabellen erstellt werden.

    while True:  # Endlosschleife, um das Menü immer wieder anzuzeigen, bis der Benutzer es beendet.
        print("1. Neuen Spieler hinzufügen")
        print("2. Rangliste anzeigen")
        print("3. Punkte eines Spielers aktualisieren")
        print("4. Spieler löschen")
        print("5. Alle Punkte zurücksetzen")
        print("6. Spieler suchen")
        print("7. Beenden")
        choice = input("Wähle eine Option: ")  # Benutzer wählt eine Option.

        if choice == '1':  # Neuen Spieler hinzufügen.
            name = input("Name des Spielers: ")
            score = get_integer_input("Punktezahl des Spielers: ")
            add_player(name, score)  # Spieler wird zur Datenbank hinzugefügt
            print(f"Spieler {name} mit der Punktzahl {score} wurde hinzugefügt.")  # Bestätigung der Spielerhinzufügung

        elif choice == '2':  # Rangliste anzeigen.
            players = get_all_players()  # Alle Spieler aus der Datenbank abrufen
            for player in players:
                print(player)  # Ausgabe jedes Spielers auf der Rangliste

        elif choice == '3':  # Punkte eines Spielers aktualisieren.
            player_id = get_integer_input("ID des Spielers: ")  # ID des Spielers abfragen
            new_score = get_integer_input("Neue Punktezahl: ")  # Neue Punktzahl abfragen
            if not update_player_score(player_id, new_score):  # Versuchen, die Punktzahl zu aktualisieren
                print(f"Kein Spieler mit der ID {player_id} gefunden.")  # Fehlermeldung, falls die ID nicht gefunden wird

        elif choice == '4':  # Spieler löschen.
            player_id = get_integer_input("ID des zu löschenden Spielers: ")  # ID des zu löschenden Spielers abfragen
            confirm = input(f"Bist du sicher, dass du den Spieler mit der ID {player_id} löschen möchtest? (ja/nein): ")
            if confirm.lower() == 'ja':  # Bestätigung des Nutzers zum Löschen
                if delete_player(player_id):  # Löschen des Spielers, wenn er existiert
                    print(f"Spieler {player_id} wurde gelöscht.")  # Erfolgsmeldung
                else:
                    print(f"Spieler mit der ID {player_id} existiert nicht.")  # Fehlermeldung, wenn der Spieler nicht existiert
            else:
                print("Löschvorgang abgebrochen.")  # Nachricht, wenn der Nutzer den Löschvorgang abbricht

        elif choice == '5':  # Alle Punkte zurücksetzen.
            confirm = input("Bist du sicher, dass du alle Punkte zurücksetzen möchtest? (ja/nein): ")
            if confirm.lower() == 'ja':  # Bestätigung des Nutzers
                reset_all_scores()  # Alle Punktzahlen werden zurückgesetzt
                print("Alle Punkte wurden zurückgesetzt.")  # Erfolgsmeldung
            else:
                print("Zurücksetzen abgebrochen.")  # Nachricht, wenn der Nutzer den Vorgang abbricht

        elif choice == '6':  # Spieler suchen.
            search_query = input("Gib den Namen des Spielers ein, den du suchen möchtest: ")  # Suchanfrage nach dem Spielernamen
            found_players = search_player(search_query)  # Spieler in der Datenbank suchen
            if found_players:
                for player in found_players:
                    print(player)  # Gefundene Spieler anzeigen
            else:
                print(f"Kein Spieler mit dem Namen {search_query} gefunden.")  # Fehlermeldung, wenn kein Spieler gefunden wurde

        elif choice == '7':  # Programm beenden.
            print("Programm wird beendet.")  # Nachricht, dass das Programm beendet wird
            sys.exit()  # Programm beenden und SystemExit auslösen

        else:
            print("Ungültige Auswahl. Bitte wähle eine gültige Option.")  # Fehlermeldung bei ungültiger Menüoption

# Der Einstiegspunkt für das Programm, wenn es als eigenständige Anwendung ausgeführt wird.
if __name__ == "__main__":
    main()
