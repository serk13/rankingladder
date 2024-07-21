# Import der benötigten Funktionen aus der database.py Datei für die Interaktion mit der Datenbank.
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
            add_player(name, score)
        elif choice == '2':  # Rangliste anzeigen.
            players = get_all_players()
            for player in players:
                print(player)
        elif choice == '3':  # Punkte eines Spielers aktualisieren.
            player_id = get_integer_input("ID des Spielers: ")
            new_score = get_integer_input("Neue Punktezahl: ")
            if not update_player_score(player_id, new_score):
                print(f"Kein Spieler mit der ID {player_id} gefunden.")
        elif choice == '4':  # Spieler löschen.
            player_id = get_integer_input("ID des zu löschenden Spielers: ")
            delete_player(player_id)
            print(f"Spieler {player_id} wurde gelöscht.")
        elif choice == '5':  # Alle Punkte zurücksetzen.
            reset_all_scores()
            print("Alle Punkte wurden zurückgesetzt.")
        elif choice == '6':  # Spieler suchen.
            search_query = input("Gib den Namen des Spielers ein, den du suchen möchtest: ")
            found_players = search_player(search_query)
            if found_players:
                for player in found_players:
                    print(player)
            else:
                print("Kein Spieler gefunden.")
        elif choice == '7':  # Beenden des Programms.
            break
        else:
            print("Ungültige Auswahl.")  # Fehlermeldung bei ungültiger Menüauswahl.

# Der Einstiegspunkt für das Programm, wenn es als eigenständige Anwendung ausgeführt wird.
if __name__ == "__main__":
    main()
