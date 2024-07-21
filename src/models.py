# Importieren notwendiger Komponenten von SQLAlchemy für die Datenbankmodellierung und -verbindung.
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Erstellen einer Basis-Klasse für die Modelle durch den Aufruf der Funktion `declarative_base()`.
# Alle Modelle, die von dieser Klasse erben, werden Teil des SQLAlchemy ORM-Systems.
Base = declarative_base()

# Definition der Klasse Player, die von Base erbt. Diese Klasse repräsentiert die Tabelle 'players' in der Datenbank.
class Player(Base):
    __tablename__ = 'players'  # Name der Tabelle in der Datenbank
    id = Column(Integer, primary_key=True)  # Eine Spalte 'id' als Primärschlüssel, automatisch inkrementiert
    name = Column(String)  # Eine Spalte 'name' für den Namen des Spielers
    score = Column(Integer)  # Eine Spalte 'score' für die Punktzahl des Spielers

    # Eine spezielle Methode, die definiert, wie eine Instanz der Klasse Player als String dargestellt wird.
    # Nützlich für Debugging und Logging.
    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Score: {self.score}"

# Einrichtung der Datenbankverbindung und Session-Management.
# 'sqlite:///rankingladder.db' gibt an, dass eine SQLite-Datenbank verwendet wird, die im gleichen Verzeichnis wie das Skript gespeichert ist.
engine = create_engine('sqlite:///rankingladder.db')

# Konfiguration einer Session-Fabrik, die mit dem oben definierten Engine-Objekt verbunden ist.
# Eine Session ermöglicht es uns, Operationen in der Datenbank zu starten und durchzuführen.
Session = sessionmaker(bind=engine)
