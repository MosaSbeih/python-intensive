from dataclasses import dataclass


@dataclass
class Point:

    x: int = 0
    y: int = 0

    def to_tuple(self) -> tuple:
        return self.x, self.y
