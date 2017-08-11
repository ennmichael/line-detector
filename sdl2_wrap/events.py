#!/usr/bin/env python3


import sdl2
from typing import Callable


Event = Callable[[sdl2.SDL_Event], bool]


def mouse_click(sdl_event: sdl2.SDL_Event) -> bool:
    return sdl_event.type == sdl2.SDL_MOUSEBUTTONDOWN and \
           sdl_event.button.button == sdl2.SDL_BUTTON_LEFT


def mouse_release(sdl_event: sdl2.SDL_Event) -> bool:
    return sdl_event.type == sdl2.SDL_MOUSEBUTTONUP and \
           sdl_event.button.button == sdl2.SDL_BUTTON_LEFT


def mouse_motion(sdl_event: sdl2.SDL_Event) -> bool:
    return sdl_event.type == sdl2.SDL_MOUSEMOTION


def user_quit(sdl_event: sdl2.SDL_Event) -> bool:
    return sdl_event.type == sdl2.SDL_QUIT


def anything(_: sdl2.SDL_Event) -> bool:
    return True
