#!/usr/bin/env python3


import sdl2


def show_message(*, title: bytes, text: bytes) -> None:
    sdl2.SDL_ShowSimpleMessageBox(0, title, text, None)
