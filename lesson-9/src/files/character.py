"""
Contains classes for our future MMORPG
"""
from logging import Logger
import doctest


class Character:
    """A class representing a game character

    Attributes:
    ----------
    name : str
        Name for the character
    hp : int
        Character max hit points
    dmg : int
        Character strength
    logger : Logger
        logging object

    Methods:
    -------
    is_alive()
        Checks if the character have positive health points
    attack(enemy=Character("enemy", 100, 50, logger))
        Reduces the hit point of an enemy
    """

    def __init__(self, name: str, hp: int, dmg: int, logger: Logger):
        """

        :param name: str :
            Name for the character
        :param hp: int :
            Character max hit points
        :param dmg: int :
            Character strength
        :param logger: Logger :
            logging object
        """
        self.name = name
        self.hit_point = hp
        self.damage = dmg
        self.logger = logger

    def is_alive(self) -> bool:
        """Checks if the character have positive health points

        Returns:
            bool: _description_

        >>> entity_logger = Logger(name="")
        >>> entity_1 = Character("Human", 100, 1, entity_logger)
        >>> entity_2 = Character("Human", 0, 1, entity_logger)
        >>> entity_1.is_alive()
        True
        >>> entity_2.is_alive()
        False
        """
        alive = self.hit_point > 0
        if not alive:
            self.logger.info(f'{self.name} is Defeated')
        return alive

    def attack(self, enemy: "Character") -> None:
        """Reduces the hit point of an enemy

        Args:
            enemy (Character): Enemy to reduce hit points

        Raises:
            ValueError: Raises when enemy is not passed

        >>> entity_logger = Logger(name="")
        >>> entity_1 = Character("Human", 100, 1, entity_logger)
        >>> entity_2 = Character("Zombie", 100, 100, entity_logger)
        >>> entity_2.attack(entity_1)

        >>> entity_1.hit_point
        0
        >>> entity_2.attack()
        Traceback (most recent call last):
            ...
        TypeError: Character.attack() missing 1 required positional argument: 'enemy'
        >>> entity_2.attack(None)
        Traceback (most recent call last):
            ...
        ValueError: Missing enemy Character
        """
        if not enemy:
            raise ValueError("Missing enemy Character")

        enemy.hit_point -= self.damage
        self.logger.info(f"{self.name} attacked {enemy.name}")


if __name__ == "__main__":
    doctest.testmod()
