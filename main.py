import pygame
import globals
from scenemanager import SceneManager


def main():
    pygame.init()
    screen = pygame.display.set_mode(globals.SCREEN_SIZE)
    pygame.display.set_caption("zPlayer")
    running = True

    manager = SceneManager()

    while running:
        event = pygame.event.wait()

        if event.type is pygame.QUIT:
            print "bye"
            running = False

        manager.current_scene.handle_events(event)
        manager.current_scene.update()
        manager.current_scene.render(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
