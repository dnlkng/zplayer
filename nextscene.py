import pygame
from pygame import *
from scene import Scene

class Next_Scene(Scene):
	"""Scene for Splashscreen"""
	def __init__(self):
		super(Next_Scene, self).__init__()
		self.bg = Surface((320, 240))
		self.bg.fill(Color("#fdf6e3"))
		self.font = pygame.font.SysFont('Arial', 64)
		self.text = self.font.render("Next", True, (211, 54, 130))

	def render(self, screen):
		screen.blit(self.bg, (0, 0))
		screen.blit(self.text, (2, 5))

	def update(self):
		raise NotImplementedError

	def handle_events(self):
		raise NotImplementedError