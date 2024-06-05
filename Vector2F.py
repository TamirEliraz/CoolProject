from __future__ import annotations

from math import sqrt


class Vector2F:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float) -> None:
        self._x = float(x)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = float(y)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f'({self.x:.2f}, {self.y:.2f})'

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other: Vector2F) -> Vector2F:
        return Vector2F(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2F) -> Vector2F:
        return self + (other * -1)

    def __mul__(self, other: int or float) -> Vector2F:
        return Vector2F(self.x * other, self.y * other)

    def __eq__(self, other: Vector2F) -> bool:
        return self.x == other.x and self.y == other.y

    def distance(self, other: Vector2F) -> float:
        return sqrt((self.y - other.y) ** 2 + (self.x - other.x) ** 2)

    def __copy__(self) -> Vector2F:
        return Vector2F(x=self.x, y=self.y)