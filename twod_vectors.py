import math

class Vector2D:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self._x = new_x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        self._y = new_y

    def add(self, other):
        nx = self._x + other.x
        ny = self._y + other.y
        return Vector2D(nx, ny)
    
    def subtract(self, other):
        nx = self._x - other.x
        ny = self._y - other.y
        return Vector2D(nx, ny)
    
    def multiply(self, scalar: float):
        return Vector2D(self._x * scalar, self._y * scalar)
    
    def dot(self, other):
        return (self._x * other.x) + (self._y * other.y)
    
    def magnitude(self):
        return math.sqrt((self._x**2) + (self._y**2))
    
    def __str__(self):
        return f"({self._x}, {self._y})"
    
    def __repr__(self):
        return f"Vector2D(x={self._x}, y={self._y})"
