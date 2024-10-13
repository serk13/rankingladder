### Kurze Beschreibung

Die `rankingladder`-Software ist ein leistungsstarkes Tool zur Verwaltung von Ranglisten und Spielergebnissen. Sie ermöglicht es, Spieler zu einem System hinzuzufügen, ihre Punktzahlen zu verfolgen, Ranglisten zu erstellen und Spielerinformationen basierend auf verschiedenen Kriterien abzurufen oder zu aktualisieren.
Die Software wurde entwickelt, um einfache und effiziente Verwaltung von Wettbewerben, Turnieren oder Ligen zu ermöglichen.
Sie bietet eine benutzerfreundliche Schnittstelle für die Verwaltung von Spielerstatistiken und unterstützt die Erstellung von dynamischen Ranglisten, die sich automatisch aktualisieren, wenn sich die Punktzahlen der Spieler ändern.

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

#### 5. Anleitung Code testen

Um die Stabilität und Zuverlässigkeit der `rankingladder`-Software sicherzustellen, ist das regelmässige Ausführen von Tests unerlässlich. Die Software nutzt Unit-Tests und Integrationstests, die mit dem Test-Framework `pytest` erstellt wurden. Es wird empfohlen, alle Tests auszuführen, bevor Änderungen an der Software vorgenommen oder neue Funktionen implementiert werden.

##### Voraussetzungen für Tests:

Stelle sicher, dass alle Abhängigkeiten für das Projekt installiert sind, indem du den folgenden Befehl ausführst:

```bash
poetry install
```

Dies stellt sicher, dass `pytest` und alle weiteren Test-Bibliotheken in der Umgebung vorhanden sind.

1. **Testumgebung aktivieren**

   Aktiviere die virtuelle Umgebung, die von `poetry` erstellt wurde, um sicherzustellen, dass alle Pakete und Abhängigkeiten korrekt verwendet werden:

   ```bash
   poetry shell
   ```

2. **Unit-Tests und Integrationstests ausführen**

   Die Tests für die Anwendung befinden sich im Verzeichnis `tests`. Um alle Tests auszuführen, nutze den folgenden Befehl:

   ```bash
   pytest
   ```

   Dieser Befehl führt alle im Projekt vorhandenen Tests aus, um sicherzustellen, dass alle Funktionen der Anwendung wie erwartet arbeiten.

3. **Tests in PyCharm ausführen**

   Falls du die Tests in der Entwicklungsumgebung PyCharm ausführen möchtest, stelle sicher, dass das Projekt korrekt als Poetry-Projekt konfiguriert ist. PyCharm erkennt dann automatisch `pytest` als Testframework. Du kannst einzelne Testdateien oder Methoden direkt aus der IDE starten, indem du auf das grüne Abspiel-Symbol neben den Testfunktionen klickst.

4. **Testabdeckung prüfen**

   Um die Testabdeckung zu prüfen, kannst du `pytest` mit dem Coverage-Plugin verwenden. Führe dazu folgenden Befehl aus:

   ```bash
   pytest --cov=src
   ```

   Dieser Befehl zeigt an, welche Teile des Codes getestet wurden und gibt dir Hinweise darauf, wo möglicherweise noch Tests fehlen.

Durch die Nutzung von `pytest` und der Integration in PyCharm kannst du sicherstellen, dass der Code stabil bleibt und alle Funktionen korrekt arbeiten.


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

- **Datenbank**: Die Anwendung verwendet standardmässig eine SQLite-Datenbank (`rankingladder.db`), die im Projektverzeichnis erstellt wird. SQLAlchemy wird als ORM verwendet, um die Interaktion mit der Datenbank zu verwalten und zu vereinfachen
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
   - **Verbesserungsvorschlag**: Die Implementierung von Dependency Injection (DI) würde die Flexibilität erhöhen. Dies könnte durch die Verwendung von `FastAPI` und Pydantic für die Konfiguration erfolgen.

3. **API-Router und Endpunkte**:
   - **Aktueller Zustand**: Im `rankingladder`-Projekt gibt es noch keinen klar definierten API-Router.
   - **Verbesserungsvorschlag**: API-Router sollten für verschiedene Funktionalitäten wie `players`, `scores` und `matches` eingeführt werden. Dies verbessert die Erweiterbarkeit und Lesbarkeit des Codes, insbesondere wenn die Anzahl der Endpunkte wächst.

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

9. **Einbindung einer "Confest.py" Datei**:
   - **Aktueller Zustand**: Datenbankinitialisierungen erfolgen bei den Tests in den benötigten Klassen.
   - **Verbesserungsvorschlag**: Beim Ausbau des Projekts wäre es sinnvoll, die Initialisierungen über eine zentrale Datei (`conftest.py`) zu definieren, um die Wiederverwendbarkeit und Wartbarkeit zu verbessern.

10. **Einbindung einer "Tournament-Rule"-Klasse**:
    - **Aktueller Zustand**: Der Punktestand wird manuell im System hinzugefügt.
    - **Verbesserungsvorschlag**: Verschiedene Turniere verwenden unterschiedliche Punktvergabelogiken. Die Logiken könnten im Projekt definiert und anschliessend aktiviert oder deaktiviert werden, sodass die Punkteberechnung automatisch anhand des Match-Outcomes erfolgt.

11. **Kompatibilität mit SQLAlchemy 2.0 sicherstellen**:
    - **Aktueller Zustand**: Der Code verwendet einige veraltete Funktionen, die in SQLAlchemy 2.0 nicht mehr unterstützt werden.
    - **Verbesserungsvorschlag**: Um die Zukunftssicherheit des Projekts zu gewährleisten, sollte der Code kompatibel mit SQLAlchemy 2.0 gemacht werden. Momentan wird die Version in der `.toml`-Datei auf `<2.0` begrenzt, um sicherzustellen, dass veraltete API-Features weiterhin unterstützt bleiben. Langfristig sollte jedoch der Code so angepasst werden, dass er die neuen APIs von SQLAlchemy 2.0 verwendet.

12. **Spieler löschen Funktion verbessern**:
   - **Aktueller Zustand**: Derzeit kann die Funktion "Spieler löschen" eine negative Spieler-ID akzeptieren, was nicht passieren sollte.
   - **Verbesserungsvorschlag**: Spieler mit negativen IDs sollten als ungültige Eingaben interpretiert und abgelehnt werden. Diese Prüfung sollte noch implementiert werden, um die Datenintegrität zu gewährleisten.

13. **Fehlermeldungen und Benutzerführung verbessern**:
   - **Aktueller Zustand**: Die Fehlermeldungen im Programm sind nicht ausführlich genug und bieten wenig Unterstützung für den Benutzer.
   - **Verbesserungsvorschlag**: Die Fehlermeldungen sollten ausführlicher gestaltet werden, um den Benutzern genauere Hinweise auf Eingabefehler oder notwendige Korrekturen zu geben. Eine benutzerfreundlichere Fehlerbehandlung würde die Usability der Anwendung erhöhen.

14. **Transaktionsmanagement optimieren**:
   - **Aktueller Zustand**: Für jede einzelne Datenbankoperation wird eine eigene Sitzung verwendet, was zu einer erhöhten Datenbanklast führen kann.
   - **Verbesserungsvorschlag**: Das Transaktionsmanagement könnte optimiert werden, indem mehrere Operationen in einer Sitzung zusammengefasst werden. Dadurch würde die Datenbanklast verringert und die Konsistenz der Daten erhöht.
   
15. **Performance-Optimierung durch Indexierung**:
   - **Aktueller Zustand**: Die Datenbankabfragen, insbesondere die Suche nach Spielern und das Abrufen aller Spieler, können bei einer grossen Anzahl von Datensätzen langsam sein.
   - **Verbesserungsvorschlag**: Die Leistung der Datenbank könnte verbessert werden, indem für häufig abgefragte Felder, wie die Spieler-ID und den Namen, Indizes hinzugefügt werden. Dies würde die Geschwindigkeit von Abfragen erhöhen und die Performance des Systems verbessern.

16. **Backup- und Wiederherstellungsmechanismus implementieren**:
   - **Aktueller Zustand**: Aktuell gibt es keine Möglichkeit, die Datenbank regelmässig zu sichern oder im Falle eines Fehlers wiederherzustellen.
   - **Verbesserungsvorschlag**: Ein automatisierter Backup-Mechanismus sollte implementiert werden, um regelmässige Sicherungen der Datenbank durchzuführen. Dies würde die Datenintegrität schützen und sicherstellen, dass im Falle eines Fehlers oder Datenverlusts eine Wiederherstellung möglich ist.

17. **Rollenbasierte Zugriffskontrolle einführen**:
   - **Aktueller Zustand**: Derzeit gibt es keine rollenbasierte Zugriffskontrolle, sodass jeder Benutzer vollen Zugriff auf alle Funktionen hat.
   - **Verbesserungsvorschlag**: Eine rollenbasierte Zugriffskontrolle sollte eingeführt werden, um sicherzustellen, dass nur autorisierte Benutzer bestimmte Aktionen ausführen können. Zum Beispiel könnten Administratoren die Berechtigung haben, Spieler zu löschen, während normale Benutzer nur ihre eigenen Daten sehen und aktualisieren können.

18. **Automatisierte Tests erweitern**:
   - **Aktueller Zustand**: Die bestehenden Tests decken einige Funktionen ab, aber nicht alle Szenarien sind abgedeckt. (Test-coverage aktuell bei 73%)
   - **Verbesserungsvorschlag**: Die Testabdeckung sollte erweitert werden, insbesondere um Grenzfälle und Fehlerbedingungen abzudecken. Automatisierte Integrationstests könnten eingeführt werden, um sicherzustellen, dass die verschiedenen Module korrekt zusammenarbeiten und um Regressionen in der Funktionalität zu vermeiden.

16. **Optimierung der Benutzeroberfläche**:
   - **Aktueller Zustand**: Das Projekt verfügt über keine grafische Benutzeroberfläche (GUI), sondern wird ausschließlich über die Kommandozeile bedient.
   - **Verbesserungsvorschlag**: Die Entwicklung einer einfachen GUI könnte die Benutzererfahrung erheblich verbessern und das Programm für weniger technikaffine Nutzer zugänglicher machen. Eine GUI könnte mit Frameworks wie Tkinter oder PyQt erstellt werden.

17. **Erweiterung der Spielerstatistiken**:
   - **Aktueller Zustand**: Derzeit werden nur der Name und die Punktzahl der Spieler verwaltet.
   - **Verbesserungsvorschlag**: Die Spielerstatistiken könnten erweitert werden, um zusätzliche Informationen wie Spielhistorie, gewonnene Turniere und persönliche Bestleistungen zu erfassen. Dies würde die Anwendungsvielfalt erhöhen und mehr Daten für Analysen zur Verfügung stellen.
#