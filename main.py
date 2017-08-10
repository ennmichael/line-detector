#!/usr/bin/env python3


import sdl2_wrap
import mouse


TRACKING_DISTANCE = 10


def main():
    with sdl2_wrap.Window('line detector', (500, 500)) as window, sdl2_wrap.Renderer(window) as renderer:
        event_loop = sdl2_wrap.EventLoop()

        m = mouse.Mouse(event_loop, TRACKING_DISTANCE)

        window.show()


if __name__ == '__main__':
    main()
