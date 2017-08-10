#!/usr/bin/env python3


import sdl2
import sdl2.ext
from typing import Any


class Renderer(sdl2.ext.Renderer):

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        sdl2.SDL_DestroyRenderer(self.sdlrenderer)


class Window(sdl2.ext.Window):

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        sdl2.SDL_DestroyWindow(self.window)
