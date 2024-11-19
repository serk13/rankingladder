# Erster Schritt: Verwenden von Poetry, um die Abhängigkeiten zu verwalten und requirements.txt zu erstellen
FROM python:3.12-slim AS builder
WORKDIR /tmp

# Installiere Poetry
RUN pip install poetry

# Kopiere die Poetry-Dateien ins temporäre Verzeichnis
COPY ./pyproject.toml ./poetry.lock ./

# Exportiere die Abhängigkeiten in eine requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev

# Zweiter Schritt: Erstellen des endgültigen Images mit nur den notwendigen Dateien
FROM python:3.12-slim
WORKDIR /app

# Kopiere die requirements.txt aus dem Builder-Image
COPY --from=builder /tmp/requirements.txt .

# Installiere die Abhängigkeiten mit pip
RUN pip install -r requirements.txt

# Entferne die requirements.txt, um Platz zu sparen
RUN rm requirements.txt

# Kopiere nur den Inhalt des 'src'-Ordners in das Image
COPY ./src /app

# Setze den Startbefehl für die FastAPI-Anwendung
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Öffne den Port 8000
EXPOSE 8000
