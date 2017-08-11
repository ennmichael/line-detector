#!/usr/bin/env python3


import sdl2_wrap
import detection


TRACKING_DISTANCE = 10


def main():
    with sdl2_wrap.Window('line detector', (500, 500)) as window, sdl2_wrap.Renderer(window) as renderer:
        event_loop = sdl2_wrap.EventLoop.with_default_quit_handling()
        window.show()
        renderer.color = sdl2_wrap.colors.WHITE
        detection.start_main_loop(
            event_loop=event_loop,
            renderer=renderer,
            tracking_distance=TRACKING_DISTANCE,
            stroke_color=sdl2_wrap.colors.BLACK)


if __name__ == '__main__':
    main()
