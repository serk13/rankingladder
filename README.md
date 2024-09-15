### Kurze Beschreibung

Die `rankingladder`-Software ist ein leistungsstarkes Tool zur Verwaltung von Ranglisten und Spielergebnissen. Sie ermöglicht es, Spieler zu einem System hinzuzufügen, ihre Punktzahlen zu verfolgen, Ranglisten zu erstellen und Spielerinformationen basierend auf verschiedenen Kriterien abzurufen oder zu aktualisieren. Die Software wurde entwickelt, um einfache und effiziente Verwaltung von Wettbewerben, Turnieren oder Ligen zu ermöglichen. Sie bietet eine benutzerfreundliche Schnittstelle für die Verwaltung von Spielerstatistiken und unterstützt die Erstellung von dynamischen Ranglisten, die sich automatisch aktualisieren, wenn sich die Punktzahlen der Spieler ändern.

### Anleitung: Start, Tests und Nutzung der `rankingladder`-Software

#### 1. Voraussetzungen

Bevor die `rankingladder`-Software gestartet wird, stelle sicher, dass folgende Software und Bibliotheken auf deinem System installiert sind:

- **Python 3.8 oder höher**
- **Poetry** (Python Package Installer)
- **Virtualenv** (optional, aber empfohlen für eine isolierte Python-Umgebung)

#### 2. Projekt einrichten

1. **Repository klonen**:

   ```bash
   git clone <repository-url>
   cd rankingladder
   ```

2. **Virtuelle Umgebung erstellen und aktivieren** (optional, aber empfohlen):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:

   Stelle sicher, dass du alle benötigten Pakete installierst, indem du den folgenden Befehl ausführst:

   ```bash
   poetry update
   ```

#### 3. Datenbank initialisieren

Bevor du die Anwendung startest, muss die Datenbank initialisiert werden:

1. **Datenbank initialisieren**:

   ```bash
   python -c "from src.database import init_db; init_db()"
   ```

   Dieser Befehl erstellt die erforderlichen Tabellen in der SQLite-Datenbank basierend auf den definierten Modellen.

#### 4. Anwendung starten

Die Anwendung kann direkt über das Terminal gestartet werden:

1. **Anwendung starten**:

   ```bash
   python src/main.py
   ```
	***ACHTUNG: Aktueller Zustand keine API verwendung. Die API verwendungen habe ich bereits aufgelistet, falls das Tool später mit einer API ergänzt wird***
   Dadurch wird der Webserver gestartet und die API ist unter `http://127.0.0.1:8000` erreichbar.

#### 5. Tests ausführen

Um sicherzustellen, dass alles korrekt funktioniert, kannst du die vorhandenen Tests ausführen:

1. **Pytest installieren** (falls noch nicht geschehen):

   ```bash
   poetry install pytest
   ```

2. **Tests ausführen**:

   ```bash
   pytest
   ```

   Diese Tests überprüfen die grundlegende Funktionalität der Anwendung, einschliesslich der Datenbanklogik und der Modelle.

#### 6. Nutzung der API
***ACHTUNG: Aktueller Zustand keine API verwendung. Die API verwendungen habe ich bereits aufgelistet, falls das Tool später mit einer API ergänzt wird***
Nachdem die Anwendung läuft, kannst du die API nutzen. Hier sind einige grundlegende Endpunkte:

- **Spieler hinzufügen**:
  
  - POST `/players/` 
  - Body: `{ "name": "Spielername", "score": Punktzahl }`

- **Alle Spieler abrufen**:
  
  - GET `/players/`

- **Spielerpunktzahl aktualisieren**:
  
  - PUT `/players/{id}` 
  - Body: `{ "score": neue Punktzahl }`

- **Spieler löschen**:
  
  - DELETE `/players/{id}`

#### 7. Wichtige Hinweise

- **Datenbank**: Die Anwendung verwendet standardmässig eine SQLite-Datenbank (`rankingladder.db`), die im Projektverzeichnis erstellt wird.
- **Konfiguration**: Anpassungen an der Datenbankverbindung und anderen Einstellungen können in den entsprechenden Konfigurationsdateien vorgenommen werden.
- **Dokumentation**: Die API-Dokumentation ist über den `/docs`-Endpunkt verfügbar, sobald der Server läuft.

### Beschreibung einzelner Komponenten der `rankingladder`-Software

Die `rankingladder`-Software ist in mehrere Komponenten unterteilt, die zusammen eine flexible und erweiterbare Architektur bilden. Im Folgenden werden die wichtigsten Komponenten detailliert beschrieben:

#### 1. `models.py`
**Funktion**: Die `models.py`-Datei definiert die Datenbankmodelle der Anwendung, die mit SQLAlchemy erstellt wurden.

- **`Player`-Modell**: Dieses Modell repräsentiert die Spieler in der Datenbank. Es enthält Felder für die `id`, den `name` und die `score` (Punktzahl) des Spielers. Das `Player`-Modell wird verwendet, um die Spielerinformationen in der Datenbank zu speichern und zu verwalten.

#### 2. `database.py`
**Funktion**: Diese Datei enthält die Datenbanklogik und ist verantwortlich für die Interaktion mit der Datenbank.

- **Initialisierung**: Die `init_db()`-Funktion erstellt alle Tabellen in der Datenbank, die durch die Modelle definiert wurden.
- **CRUD-Operationen**: Es gibt Funktionen zum Erstellen, Lesen, Aktualisieren und Löschen (CRUD) von Spielerinformationen. Beispiele sind `add_player()`, `get_all_players()`, `update_player_score()` und `delete_player()`.
- **Spezielle Operationen**: Es gibt auch spezielle Funktionen wie `reset_all_scores()` (zum Zurücksetzen der Punktzahlen aller Spieler) und `search_player()` (zum Suchen von Spielern nach Namen).

#### 3. `main.py`
**Funktion**: Dies ist der Einstiegspunkt der Anwendung und enthält die Logik für die API-Endpunkte.

- **API-Endpunkte**: In `main.py` sind dann zukünftig die verschiedenen API-Routen definiert, die die Kernfunktionen der Anwendung verfügbar machen. Hier werden die Routen zur Verwaltung der Spieler über HTTP-Anfragen bereitgestellt.
- **FastAPI**: Die Anwendung nutzt `FastAPI` als Webframework, das eine einfache und schnelle Entwicklung von RESTful APIs ermöglicht.

#### 4. `tests/`
**Funktion**: Dieses Verzeichnis enthält die Testfälle, die sicherstellen, dass die Anwendung korrekt funktioniert.

- **`test_models.py`**: Diese Datei enthält Tests für die Datenbankmodelle, um sicherzustellen, dass die Modelle korrekt definiert und verwendet werden.
- **`test_database.py`**: Diese Datei enthält Tests für die Datenbankfunktionen, um sicherzustellen, dass CRUD-Operationen und andere Datenbankinteraktionen ordnungsgemäss funktionieren.

#### 5. `routers/`, `schemas/`, `services/` (Erweiterungsmöglichkeiten)
**Funktion**: Diese Komponenten könnten in zukünftigen Versionen hinzugefügt werden, um die Modularität und Skalierbarkeit zu verbessern.

- **`routers/`**: Enthält die API-Endpunkte, unterteilt in verschiedene Module (z.B. `players`, `scores`), um die Routenverwaltung zu vereinfachen.
- **`schemas/`**: Definiert die Datenstrukturen und Validierungen mithilfe von Pydantic, die für die API-Anfragen und -Antworten verwendet werden.
- **`services/`**: Kapselt die Geschäftslogik der Anwendung, sodass die Endpunkte schlank bleiben und die Logik leicht testbar und erweiterbar ist.

### Überlegungen zum `rankingladder`-Projekt

Bei der Entwicklung der `rankingladder`-Software standen mehrere wichtige Überlegungen im Vordergrund, um eine robuste, skalierbare und "userfriendly" Anwendung zu schaffen. Im Folgenden sind die wichtigsten Punkte aufgeführt:

#### 1. **Zielsetzung und Anwendungsbereich**

Das primäre Ziel des `rankingladder`-Projekts war es, eine flexible und leicht erweiterbare Plattform zur Verwaltung von Ranglisten und Spielergebnissen zu entwickeln. Die Software sollte nicht nur für kleine Turniere und Wettkämpfe geeignet sein, sondern auch für grössere Wettbewerbe mit einer Vielzahl von Teilnehmern skalieren können.

#### 2. **Architektur und Modularität**

Eine der zentralen Überlegungen bei der Entwicklung war die Architektur des Projekts. Die Software wurde so modular aufgebaut, dass jede Komponente klar voneinander getrennt ist. Dies ermöglicht es, einzelne Teile der Anwendung unabhängig voneinander zu testen, zu warten und zu erweitern. Die Trennung in `models.py`, `database.py`, und `main.py` war ein bewusster Schritt, um sicherzustellen, dass die Datenbanklogik, die Datenmodelle und die Anwendungslogik voneinander isoliert sind.

#### 3. **Skalierbarkeit und Leistung**

Ein weiteres wichtiges Ziel war es, die Anwendung so zu gestalten, dass sie bei Bedarf leicht skalierbar ist. Durch die Nutzung von FastAPI, das sowohl synchron als auch asynchron arbeiten kann, ist die Anwendung in der Lage, auch bei hoher Last eine gute Leistung zu erbringen. In zukünftigen Versionen könnte die Anwendung weiter optimiert werden, um asynchrone Datenbankoperationen zu unterstützen.

#### 4. **Benutzerfreundlichkeit und API-Design**

Die Benutzerfreundlichkeit und das API-Design standen ebenfalls im Mittelpunkt der Überlegungen. Es wurde darauf geachtet, dass die API-Endpunkte intuitiv und leicht verständlich sind. Jede API-Ressource hat klar definierte Routen, die den CRUD-Operationen (Create, Read, Update, Delete) folgen, sodass Entwickler die API ohne grossen Aufwand integrieren können.

#### 5. **Feature Driven Developmen**

Beim erweiterung des Projektes, soll zukünftig so ausgebaut werden, dass einzelne Features alleinstehend implementiert werden können und dieses durch eine Zentrale Aktivsteuerung aktiviert und deaktiviert werden kann.

#### 6. **Erweiterbarkeit

**

Das Projekt wurde so entworfen, dass es leicht erweiterbar ist. Neue Funktionen können problemlos hinzugefügt werden, ohne die bestehende Struktur zu stören. Beispielsweise könnten zukünftige Erweiterungen wie Match-Management, fortgeschrittene Statistikmodule oder eine Benutzerverwaltung einfach integriert werden. 

#### 7. **Testbarkeit und Qualitätssicherung**

Von Anfang an wurde Wert auf Testbarkeit gelegt. Durch die klare Trennung der Logik in verschiedene Module konnten umfassende Unit-Tests geschrieben werden, um die Zuverlässigkeit der Software sicherzustellen. Die Tests decken sowohl die Datenbanklogik als auch die Modelle ab, um sicherzustellen, dass alle Kernfunktionen wie erwartet funktionieren.

#### 8. **Sicherheit und Datenintegrität**

Obwohl die aktuelle Version der Anwendung noch keine Authentifizierungs- oder Autorisierungsmechanismen implementiert hat, wurde von Anfang an bedacht, wie diese in zukünftigen Versionen integriert werden können. Darüber hinaus wurde darauf geachtet, dass alle Datenbankoperationen sicher und konsistent ablaufen, um Datenintegrität zu gewährleisten.

#### 9. **Zukunftsperspektiven**

In der Planung für zukünftige Versionen des Projekts wurden mehrere Erweiterungsmöglichkeiten in Betracht gezogen, darunter:
- Implementierung von asynchronen Funktionen für bessere Leistung.
- Einführung eines erweiterten Berechtigungssystems, um verschiedene Benutzerrollen zu unterstützen.
- Erweiterung der API, um komplexere Wettbewerbsregeln und Ranglistenlogiken zu unterstützen.

### Schritte zur Verbesserung und Erweiterung des `rankingladder`-Projekts

1. **Projektstruktur und Modularität**:
   - **Aktueller Zustand**: Das `rankingladder`-Projekt hat eine grundlegende Struktur mit getrennten Dateien für Modelle, Datenbanklogik und Hauptanwendung. Es fehlen jedoch Ordnerstrukturen, die für grössere Projekte hilfreich sein können.
   - **Verbesserungsvorschlag**: Die Ordnerstruktur könnte weiter modularisiert werden, indem separate Verzeichnisse für `routers`, `schemas`, `services` und `dependencies` erstellt werden. Diese Struktur hilft dabei, den Code besser zu organisieren und wartbarer zu machen.

2. **Einführung von Dependency Injection**:
   - **Aktueller Zustand**: Derzeit wird die Datenbankverbindung direkt im Code der Hauptanwendung und Tests erstellt.
   - **Verbesserungsvorschlag**: Die Implementierung von Dependency Injection (DI) würde die Flexibilität erhöhen. Dies könnte durch die Verwendung von `FastAPI` und Pydantic für die Konfiguration erfolgen, wie es in `services.zip` möglicherweise der Fall ist.

3. **API-Router und Endpunkte**:
   - **Aktueller Zustand**: Im `rankingladder`-Projekt gibt es noch keinen klar definierten API-Router zu geben.
   - **Verbesserungsvorschlag**: API-Router sollten für verschiedene Funktionalitäten wie `players`, `scores`, und `matches` eingeführt werden. Dies verbessert die Erweiterbarkeit und Lesbarkeit des Codes, insbesondere wenn die Anzahl der Endpunkte wächst.

4. **Asynchrone Programmierung**:
   - **Aktueller Zustand**: Alle Datenbankoperationen sind synchron, was die Leistung bei einer hohen Anzahl gleichzeitiger Anfragen beeinträchtigen könnte.
   - **Verbesserungsvorschlag**: Die Umstellung auf asynchrone Programmierung unter Verwendung von `asyncio` und `FastAPI` könnte die Skalierbarkeit und Leistung verbessern.

5. **Erweiterte Fehlerbehandlung und Logging**:
   - **Aktueller Zustand**: Es gibt eine grundlegende Fehlerbehandlung, aber kein systematisches Logging.
   - **Verbesserungsvorschlag**: Die Einführung eines Logging-Systems und einer besseren Fehlerbehandlung (z.B. mit benutzerdefinierten Exception-Handling-Middleware) würde die Diagnose und Wartung erleichtern.

6. **Testabdeckung und Continuous Integration (CI)**:
   - **Aktueller Zustand**: Es gibt Tests, aber die Abdeckung könnte erweitert und verbessert werden.
   - **Verbesserungsvorschlag**: Die Testabdeckung sollte auf alle wichtigen Funktionalitäten ausgeweitet werden, einschliesslich Integrationstests für die API. Eine CI/CD-Pipeline könnte eingerichtet werden, um die Qualitätssicherung zu automatisieren.

7. **Datenvalidierung und Sicherheit**:
   - **Aktueller Zustand**: Die Validierung von Eingabedaten und Sicherheit ist begrenzt.
   - **Verbesserungsvorschlag**: Mit Pydantic-Modellen könnte eine strikte Validierung eingeführt werden. Zudem könnten Sicherheitsmassnahmen wie Authentifizierung und Autorisierung integriert werden.

8. **Dokumentation und API-Dokumentation**:
   - **Aktueller Zustand**: Die Dokumentation des Projekts ist minimal.
   - **Verbesserungsvorschlag**: Eine detaillierte API-Dokumentation (z.B. mit Swagger/OpenAPI) und eine erweiterte Projektdokumentation im README, die Installationsanweisungen, Codebeispiele und Architekturdiagramme umfasst, sollte hinzugefügt werden.
   
9. **Einbindung einer "Confest.py Datei"**:
-    **Aktueller Zustand**: Datenbankinitialiserungen erfolgen beim Test in der benötigten Klassen.
-    **Verbesserungsvorschlag**: Beim Ausbau des Projektes, wäre es sinnvoll eventuell die Initialsierungen über eine Zentrale Klassen zu definieren.

10. **Einbindung Torunament-Rule-Klasse"**:
-    **Aktueller Zustand**: Der Punktestand wird manuell im System hinzugefügt.
-    **Verbesserungsvorschlag**: Verschiede Tournaments verwenden verschieden Punktevergabenlogiken. Die Logiken können im Projekt definiert werdnen und anschliessend aktivieret oder deaktiviert werden. Anschliessend passiert die Punkteberechnung automatisch anhand vom "Outcome" des Matches.

#