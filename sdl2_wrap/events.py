#!/usr/bin/env python3


import sdl2
import abc
from typing import Tuple, Any


class Event(abc.ABC):

    def __init__(self, callback: Any) -> None:
        self.__callback = callback

    def dispatch(self, raw_event: sdl2.SDL_Event) -> None:
        if self._should_dispatch(raw_event):
            self.__callback(*self._callback_parameters_tuple(raw_event))

    @abc.abstractmethod
    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        pass

    @abc.abstractmethod
    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Any:
        pass


class MouseClick(Event):

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        return raw_event.type == sdl2.SDL_MOUSEBUTTONDOWN and \
               raw_event.button.button == sdl2.SDL_BUTTON_LEFT

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Tuple[sdl2.SDL_Point]:
        return (mouse_position(raw_event),)


class MouseRelease(Event):

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        return raw_event.type == sdl2.SDL_MOUSEBUTTONUP

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Tuple[sdl2.SDL_Point]:
        return (mouse_position(raw_event),)


class MouseMotion(Event):

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        return raw_event.type == sdl2.SDL_MOUSEMOTION

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Tuple[sdl2.SDL_Point]:
        return (mouse_position(raw_event),)


def mouse_position(raw_event: sdl2.SDL_Event) -> sdl2.SDL_Point:
    return sdl2.SDL_Point(raw_event.button.x, raw_event.button.y)


class UserQuit(Event):

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        return raw_event.type == sdl2.SDL_QUIT

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Any:
        return ()


class Anything(Event):

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        return True

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Any:
        return ()


class AppStarted(Event):

    __dispatched = False

    def _should_dispatch(self, raw_event: sdl2.SDL_Event) -> bool:
        if not AppStarted.__dispatched:
            AppStarted.__dispatched = True
            return True
        return False

    def _callback_parameters_tuple(self, raw_event: sdl2.SDL_Event) -> Any:
        return ()
