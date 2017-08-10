#!/usr/bin/env python3


import sdl2_wrap
import sdl2
import utils
from typing import Optional, List


Stroke = List[sdl2.SDL_Point]


class Mouse:

    def __init__(self, event_loop: sdl2_wrap.EventLoop, tracking_distance: int) -> None:
        being_dragged = False
        self.stroke: List[sdl2.SDL_Point] = []

        def on_click(position: sdl2.SDL_Point) -> None:
            nonlocal being_dragged
            being_dragged = True
            self.stroke.append(position)

        def on_release(position: sdl2.SDL_Point) -> None:
            nonlocal being_dragged
            being_dragged = False
            self.stroke.append(position)

        def on_motion(position: sdl2.SDL_Point) -> None:
            if being_dragged and utils.distance(self.__last_point, position) >= tracking_distance:
                self.stroke.append(position)

        event_loop.add_event(sdl2_wrap.events.MouseClick(on_click))
        event_loop.add_event(sdl2_wrap.events.MouseRelease(on_release))
        event_loop.add_event(sdl2_wrap.events.MouseMotion(on_motion))

    @property
    def __last_point(self) -> sdl2.SDL_Point:
        return self.stroke[-1]
    sdl2.SDL_Event
