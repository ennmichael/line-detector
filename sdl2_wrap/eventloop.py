#!/usr/bin/env python3


import sdl2.ext
from . import events
from typing import Callable, Any, List, Tuple, Iterable


class ControlFlowException(Exception):
    pass


class QuitEventLoop(ControlFlowException):
    pass


EventCallback = Callable[[sdl2.SDL_Event], None]


class EventLoop:

    @staticmethod
    def with_default_quit_handling() -> Any:

        def default_quit_callback(_: sdl2.SDL_Event) -> None:
            raise QuitEventLoop

        event_loop = EventLoop()
        event_loop.on(event=events.user_quit, callbacks=[default_quit_callback])
        return event_loop

    def __init__(self) -> None:
        self.__events_and_callbacks: List[Tuple[events.Event, EventCallback]] = []

    def on(self, *, event: events.Event, callbacks: Iterable[EventCallback]) -> Any:
        self.__events_and_callbacks.extend((event, callback) for callback in callbacks)

    def run(self) -> None:
        while True:
            for sdl_event in sdl2.ext.get_events():
                try:
                    self.__dispatch_event(sdl_event)
                except QuitEventLoop:
                    return

    def __dispatch_event(self, sdl_event: sdl2.SDL_Event) -> None:
        for event, callback in self.__events_and_callbacks:
            if event(sdl_event):
                callback(sdl_event)
