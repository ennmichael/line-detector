#!/usr/bin/env python3


import math
import sdl2
from typing import NewType


def distance(p1: sdl2.SDL_Point, p2: sdl2.SDL_Point) -> float:
    """
    >>> distance(sdl2.SDL_Point(0, 0), sdl2.SDL_Point(4, 3))
    5.0
    >>> distance(sdl2.SDL_Point(0, 0), sdl2.SDL_Point(3, 4))
    5.0
    >>> distance(sdl2.SDL_Point(3, 2), sdl2.SDL_Point(8, 14))
    13.0
    """

    distances = xy_distances(p1, p2)
    return math.sqrt(distances.x**2 + distances.y**2)


def xy_distances(p1: sdl2.SDL_Point, p2: sdl2.SDL_Point) -> sdl2.SDL_Point:  # TODO Needs a better name
    return sdl2.SDL_Point(
        x_distance(p1, p2),
        y_distance(p1, p2)
    )


def x_distance(p1: sdl2.SDL_Point, p2: sdl2.SDL_Point) -> int:
    """
    >>> x_distance(sdl2.SDL_Point(0, 0), sdl2.SDL_Point(13, 33))
    13
    >>> x_distance(sdl2.SDL_Point(5, 0), sdl2.SDL_Point(13, 33))
    8
    >>> x_distance(sdl2.SDL_Point(22, 0), sdl2.SDL_Point(13, 33))
    -9
    >>> x_distance(sdl2.SDL_Point(0, 0), sdl2.SDL_Point(0, 0))
    0
    """

    return p2.x - p1.x


def y_distance(p1: sdl2.SDL_Point, p2: sdl2.SDL_Point) -> int:
    """
    >>> y_distance(sdl2.SDL_Point(0, 0), sdl2.SDL_Point(13, 33))
    33
    >>> y_distance(sdl2.SDL_Point(22, 13), sdl2.SDL_Point(13, 33))
    20
    >>> y_distance(sdl2.SDL_Point(22, 43), sdl2.SDL_Point(13, 33))
    -10
    >>> y_distance(sdl2.SDL_Point(22, 0), sdl2.SDL_Point(13, 0))
    0
    """

    return p2.y - p1.y


Rads = NewType('Rads', float)


def angle_between_points(p1: sdl2.SDL_Point, p2: sdl2.SDL_Point) -> Rads:  # TODO Write test for this
    distances = xy_distances(p1, p2)
    return Rads(math.pi/2 if distances.x == 0 else math.atan(distances.y/distances.x))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
