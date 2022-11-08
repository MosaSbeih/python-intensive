import pytest
from logging import Logger

from ..files.character import Character


@pytest.fixture
def get_logger():
    yield Logger(name="Character")


# is_alive
def test_is_alive_true(get_logger):
    entity = Character("Human", 100, 1, get_logger)
    assert entity.is_alive()


def test_is_alive_false(get_logger):
    entity = Character("Human", 0, 1, get_logger)
    assert not entity.is_alive()


# attack
def test_attack_none(get_logger):
    predator = Character("Lion", 100, 50, get_logger)
    prey = Character("Gazelle", 50, 1, get_logger)
    assert predator.attack(prey) is None


def test_attack_hp_decrement(get_logger):
    predator = Character("Lion", 100, 50, get_logger)
    prey = Character("Gazelle", 50, 1, get_logger)
    predator.attack(prey)
    assert prey.hit_point == 0


def test_attack_value_error(get_logger):
    predator = Character("Lion", 100, 50, get_logger)
    prey = None
    with pytest.raises(ValueError):
        predator.attack(prey)


def test_attack_type_error(get_logger):
    predator = Character("Lion", 100, 50, get_logger)
    with pytest.raises(TypeError):
        predator.attack()
