#!/usr/bin/env python3


import sdl2.ext
from . import events
from typing import Callable, Any, List, NamedTuple


class ControlFlowException(Exception):
    pass


class QuitEventLoop(ControlFlowException):
    pass


class EventLoop:

    @staticmethod
    def with_default_quit_handling() -> Any:

        def default_quit_callback() -> None:
            raise QuitEventLoop

        return EventLoop().add_event(events.UserQuit(default_quit_callback))

    def __init__(self) -> None:
        self.__events: List[events.Event] = []

    def add_event(self, event: events.Event) -> Any:
        self.__events.append(event)
        return self

    def run(self) -> None:
        while True:
            for raw_event in sdl2.ext.get_events():
                try:
                    self.__dispatch_events(raw_event)
                except QuitEventLoop:
                    return

    def __dispatch_events(self, raw_event: sdl2.SDL_Event) -> None:
        for event in self.__events:
            event.dispatch(raw_event)
