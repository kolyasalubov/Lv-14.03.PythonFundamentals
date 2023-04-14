from math import pi
from math import pow


def area_rectangle(length: int, width: int) -> int:
    return length * width


def area_triangle(height: int, base: int) -> float:
    return (base * height) / 2


def area_circle(radius: int) -> float:
    return pi * pow(radius, 2)
