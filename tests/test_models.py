import pytest
from src.models import Player, Base, engine

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_player_creation(setup_database):
    player = Player(name="John Doe", score=100)
    assert player.name == "John Doe"
    assert player.score == 100
    assert str(player) == "<Player(name=John Doe, score=100)>"
