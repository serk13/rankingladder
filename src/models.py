from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Basisklasse für Modelle
Base = declarative_base()

# Player-Modell, das die 'players'-Tabelle in der Datenbank repräsentiert
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Score: {self.score}"

# Einrichtung der Datenbankverbindung
engine = create_engine('sqlite:///rankingladder.db')

# Konfiguration der Session
Session = sessionmaker(bind=engine)
