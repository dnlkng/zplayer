import pygame
import globals
import time
from scenemanager import SceneManager


def main():
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

if __name__ == "__main__":
    main()
