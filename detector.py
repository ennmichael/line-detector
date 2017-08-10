#!/usr/bin/env python3


import sdl2
import utils
from typing import List, Iterable, Tuple, NewType


def point_pairs(stroke: Stroke) -> Iterable[Tuple[sdl2.SDL_Point, sdl2.SDL_Point]]:
    return ((stroke[i], stroke[i+1]) for i in range(len(stroke) - 1))


def point_angles(stroke: Stroke) -> Iterable[float]:
    return (utils.angle_between_points(p1, p2) for p1, p2 in point_pairs(stroke))
