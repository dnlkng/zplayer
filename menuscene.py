import pygame
from pygame import *
from button import Button
from scene import Scene
import glob
import globals


class MenuScene(Scene):
    """Menu scene"""

    def __init__(self, scene_manager):
        super(MenuScene, self).__init__(scene_manager)
        self.bg = Surface(globals.SCREEN_SIZE)
        self.bg.fill(Color("#fdf6e3"))
        self.font = pygame.font.SysFont('Arial', 64)
        self.text = self.font.render("Next", True, (211, 54, 130))

        self.buttons = []
        self.build_menu()

        self.has_updates = True

    def render(self, screen):
        screen.blit(self.bg, (0, 0))

        for btn in self.buttons:
            btn.draw(screen)

    def update(self):
        current_update_state = self.has_updates
        self.has_updates = False
        return current_update_state

    def handle_events(self, e):
        if e.type is pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for btn in self.buttons:
                btn.selected(pos)

    def on_button_clicked(self, folder):
        self.manager.show_player(folder)

    def build_menu(self):
        book_icon_name = "icon.png"
        path = "./audiobooks/*/"
        folders = glob.glob(path)
        icons = []

        for i, folder in enumerate(folders):
            icons.append(folder + book_icon_name)

        # 240 Breite: 240 / 3 = 80 > 80 > 10 links + 10 rechts > 60 pixel
        # 320 - 240 = 80 > links 40 rechts 40 rand

        screen_margin = 40
        x = screen_margin
        y = 10

        for i, folder in enumerate(folders):
            button = Button((x, y, 80, 80), value=folder, cb=self.on_button_clicked)
            button.iconFg = pygame.image.load(icons[i])
            if x < 200:
                x += 80
            else:
                x = 40
                y += 80

            self.buttons.append(button)
