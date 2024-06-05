from typing import Tuple
from Vector2F import Vector2F as Point
from math import sqrt


class Polynomial:
    def __init__(self, a: int or float, b: int or float, c: int or float):
        self.a: float = a
        self.b: float = b
        self.c: float = c

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, a: int or float):
        self._a = float(a)

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, b: int or float):
        self._b = float(b)

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, c: int or float):
        self._c = float(c)

    @property
    def f(self):
        return lambda x: eval(f"{self.a}*{x}*{x}+{self.b}*{x}+{self.c}")

    def y(self, x: int or float):
        return self.f(x)

    def point(self, x) -> Point:
        return Point(x, self.y(x))

    @property
    def delta(self) -> float:
        return self.b * self.b - 4 * self.a * self.c

    @property
    def s_delta(self) -> float:
        return sqrt(self.delta)

    @property
    def y_axis(self) -> Point:
        return Point(0, self.y(0))

    @property
    def x_axis(self) -> Tuple[Point] or None:
        d: float = self.delta
        if d < 0:
            return None
        elif d == 0:
            return tuple([Point(y=eval(f"(-{self.b}+{self.s_delta})/2*{self.a}"))])
        else:
            return tuple([Point(y=eval(f"(-{self.b}{s}{self.s_delta})/2*{self.a}")) for s in ['+', '-']])

    @property
    def edge(self) -> Point:
        res: Point = Point(x=-self.b / (2 * self.a))
        res.y = self.y(res.x)
        return res

    @property
    def hasMax(self) -> bool:
        return self.a < 0

    @property
    def hasMin(self) -> bool:
        return self.a > 0

    @property
    def max(self) -> Point or None:
        return self.edge if self.hasMax else None

    @property
    def min(self) -> Point or None:
        return self.edge if self.hasMin else None
