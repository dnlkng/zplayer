import pygame
from pygame import *
from scene import Scene
import globals


class Startup_Scene(Scene):
    """Scene for Splashscreen"""

    def __init__(self):
        super(Startup_Scene, self).__init__()
        self.bg = Surface(globals.SCREEN_SIZE)
        self.bg.fill(Color("#fdf6e3"))
        self.font = pygame.font.SysFont('zapfino', 64)
        self.text = self.font.render("zPlayer", True, (211, 54, 130))

    def render(self, screen):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.text, (20, 20))

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
