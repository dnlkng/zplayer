import os
import time
import pygame
import globals
from scenemanager import SceneManager


def main():
    if runs_on_pi():
        os.putenv('SDL_FBDEV', '/dev/fb1')
        os.putenv('SDL_MOUSEDRV', 'TSLIB')
        os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

    pygame.init()
    screen = pygame.display.set_mode(globals.SCREEN_SIZE)
    pygame.display.set_caption("zPlayer")
    running = True

    manager = SceneManager()

    while running:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONUP:
                manager.current_scene.handle_events(event)

            elif event.type is pygame.QUIT:
                print "bye"
                running = False

        has_updates = manager.current_scene.update()

        if has_updates:
            print "has updates"
            manager.current_scene.render(screen)
            pygame.display.flip()

        time.sleep(.2)


def runs_on_pi():
    # it's not perfect but it will do
    if os.uname()[4].startswith("arm"):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
