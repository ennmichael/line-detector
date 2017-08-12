#!/usr/bin/env python3


import sdl2


def show_message(*, title: bytes, text: bytes) -> None:
    sdl2.SDL_ShowSimpleMessageBox(0, title, text, None)


class IncorrectEvent(Exception):
    pass


def motion_position(motion_event: sdl2.SDL_Event) -> sdl2.SDL_Point:
    if motion_event.type != sdl2.SDL_MOUSEMOTION:
        raise IncorrectEvent
    return sdl2.SDL_Point(motion_event.motion.x, motion_event.motion.y)


def click_position(click_event: sdl2.SDL_Event) -> sdl2.SDL_Point:
    if click_event.type != sdl2.SDL_MOUSEBUTTONDOWN:
        raise IncorrectEvent
    return sdl2.SDL_Point(click_event.button.x, click_event.button.y)
