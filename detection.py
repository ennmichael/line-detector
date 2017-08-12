#!/usr/bin/env python3


import sdl2_wrap
import sdl2
import math
import utils
import statistics
import sdl2.ext
from typing import List, Iterable, Tuple


Stroke = List[sdl2.SDL_Point]


def paint_stroke_callback(
        renderer: sdl2_wrap.Renderer,
        stroke: Stroke,
        stroke_color: sdl2.ext.Color) -> sdl2_wrap.EventCallback:

    last_drawn_point: sdl2.SDL_Point = None

    def callback(_: sdl2.SDL_Event) -> None:
        nonlocal last_drawn_point

        if len(stroke) == 2:
            last_drawn_point = stroke[0]

        if len(stroke) > 2 and last_drawn_point is not stroke[-1]:
            renderer.draw_line((last_drawn_point.x, last_drawn_point.y, stroke[-1].x, stroke[-1].y), stroke_color)
            renderer.present()
            last_drawn_point = stroke[-1]

    return callback


def start_main_loop(
        event_loop: sdl2_wrap.EventLoop,
        renderer: sdl2_wrap.Renderer,
        tracking_distance: int,
        stroke_color: sdl2.ext.Color,
        tolerance: utils.Rads) -> None:

    stroke: Stroke = []
    tracking_stroke = False

    def start_tracking_stroke(click_event: sdl2.SDL_Event) -> None:
        nonlocal tracking_stroke
        nonlocal stroke
        stroke = [sdl2.SDL_Point(click_event.button.x, click_event.button.y)]
        tracking_stroke = True

    def add_motion_to_stroke(motion_event: sdl2.SDL_Event) -> None:
        point = sdl2_wrap.motion_position(motion_event)
        if tracking_stroke and point_can_be_added(point):
            stroke.append(point)

    def point_can_be_added(point: sdl2.SDL_Point) -> bool:
        if not stroke:
            return True
        return point_is_at_tracking_distance(point)

    def point_is_at_tracking_distance(point: sdl2.SDL_Point) -> bool:
        return utils.distance(stroke[-1], point) >= tracking_distance

    def stop_tracking_stroke(_: sdl2.SDL_Event) -> None:
        nonlocal tracking_stroke
        tracking_stroke = False

    def draw_new_point(motion_event: sdl2.SDL_Event):
        motion_position = sdl2_wrap.motion_position(motion_event)
        if tracking_stroke and point_is_at_tracking_distance(motion_position):
            renderer.draw_line((stroke[-1].x, stroke[-1].y, motion_position.x, motion_position.y), stroke_color)
            renderer.present()

    def give_feedback(_: sdl2.SDL_Event) -> None:
        if is_line(stroke, tolerance):
            print("It's a line")
        else:
            print('Not a line')

    def clear_renderer(_: sdl2.SDL_Event) -> None:
        renderer.clear()

    event_loop.on(event=sdl2_wrap.events.mouse_click, callbacks=[start_tracking_stroke, clear_renderer])
    event_loop.on(event=sdl2_wrap.events.mouse_motion, callbacks=[draw_new_point, add_motion_to_stroke])
    event_loop.on(event=sdl2_wrap.events.mouse_release, callbacks=[stop_tracking_stroke, give_feedback])

    event_loop.run()


def is_line(stroke: Stroke, tolerance: utils.Rads) -> bool:
    average_angle = average_angle_between_points(stroke)
    return all(math.isclose(average_angle, angle, abs_tol=tolerance) for angle in angles_between_points(stroke))


def average_angle_between_points(stroke: Stroke) -> utils.Rads:  # TODO Write a test for this
    return utils.Rads(statistics.mean(angles_between_points(stroke)))


def angles_between_points(stroke: Stroke) -> Iterable[utils.Rads]:  # TODO Write a test for this
    return (utils.angle_between_points(p1, p2) for p1, p2 in point_pairs(stroke))


def point_pairs(stroke: Stroke) -> Iterable[Tuple[sdl2.SDL_Point, sdl2.SDL_Point]]:
    """
    >>> list(point_pairs([
    ... sdl2.SDL_Point(0, 0),
    ... sdl2.SDL_Point(1, 0),
    ... sdl2.SDL_Point(x=2, y=1),
    ... ]))
    [(SDL_Point(x=0, y=0), SDL_Point(x=1, y=0)), (SDL_Point(x=1, y=0), SDL_Point(x=2, y=1))]
    >>> list(point_pairs([]))
    []
    """
    return ((stroke[i], stroke[i+1]) for i in range(len(stroke) - 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
