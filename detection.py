#!/usr/bin/env python3


import sdl2_wrap
import sdl2
import utils
from typing import List, Iterable, Tuple


Stroke = List[sdl2.SDL_Point]


def start_main_loop(
        event_loop: sdl2_wrap.EventLoop,
        renderer: sdl2_wrap.Renderer,
        tracking_distance: int,
        stroke_color: sdl2.SDL_Color) -> None:

    stroke: Stroke = []
    tracking_stroke = False

    def start_tracking_stroke(sdl_event: sdl2.SDL_Event) -> None:
        nonlocal tracking_stroke
        nonlocal stroke
        stroke = [sdl2.SDL_Point(sdl_event.button.x, sdl_event.button.y)]
        tracking_stroke = True

    def add_motion_to_stroke(sdl_event: sdl2.SDL_Event) -> None:
        if tracking_stroke and utils.distance(*last_two_points(stroke)) >= tracking_distance:
            stroke.append(sdl2.SDL_Point(sdl_event.motion.x, sdl_event.motion.y))

    def stop_tracking_stroke(_: sdl2.SDL_Event) -> None:
        nonlocal tracking_stroke
        tracking_stroke = False

    def give_feedback(_: sdl2.SDL_Event) -> None:
        if is_line(stroke):
            print("It's a line")
        else:
            print('Not a line')

    def redraw(_: sdl2.SDL_Event) -> None:

        def draw_stroke():
            for p1, p2 in point_pairs(stroke):
                renderer.draw_line((p1.x, p1.y, p2.x, p2.y), stroke_color)

        renderer.clear()  # TODO Redrawing everything is too inefficient for no reason, there's a better solution
        draw_stroke()
        renderer.present()

    event_loop.on(event=sdl2_wrap.events.mouse_click, callbacks=[start_tracking_stroke])
    event_loop.on(event=sdl2_wrap.events.mouse_motion, callbacks=[add_motion_to_stroke])
    event_loop.on(event=sdl2_wrap.events.mouse_release, callbacks=[stop_tracking_stroke, give_feedback])
    event_loop.on(event=sdl2_wrap.events.anything, callbacks=[redraw])
    # TODO ^ Also inefficient for no reason, don't use events.anything

    event_loop.run()


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


def point_angles(stroke: Stroke) -> Iterable[float]:  # TODO Write test for this
    return (utils.angle_between_points(p1, p2) for p1, p2 in point_pairs(stroke))


def last_two_points(stroke: Stroke) -> Tuple[sdl2.SDL_Point, sdl2.SDL_Point]:
    return stroke[-1], stroke[-2]


def is_line(stroke: Stroke) -> bool:
    pass


def average_angle(stroke: Stroke) -> utils.Rads:  # TODO Write test for this
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
