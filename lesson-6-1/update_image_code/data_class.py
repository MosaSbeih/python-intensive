from dataclasses import dataclass


@dataclass
class Point:

    x: int
    y: int

    @classmethod
    def default(cls):
        return Point(x=0, y=0)

    def to_tuple(self) -> tuple:
        return self.x, self.y
