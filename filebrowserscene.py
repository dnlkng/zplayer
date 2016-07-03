import pygame
from pygame import *
from button import Button
from scene import Scene
import glob
import globals


class FileBrowserScene(Scene):
    """Menu scene"""

    def __init__(self, scene_manager):
        super(FileBrowserScene, self).__init__(scene_manager)
        self.bg = Surface(globals.SCREEN_SIZE)
        self.bg.fill(Color("#fdf6e3"))

        self.is_for_music = False
        self.folder = ""
        self.buttons = []

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
        self.manager.show_player(folder, self.is_for_music)

    def set_folder(self, folder, is_for_music):
        self.folder = folder
        self.is_for_music = is_for_music
        self.has_updates = True
        self.build_menu()

    def go_to_main_menu(self):
        self.manager.show_main_menu()

    def build_menu(self):
        self.buttons = []

        back_button = Button((0, 0, 42, 42), cb=self.go_to_main_menu)
        back_button.iconFg = pygame.image.load("./resources/images/chevron.png")
        self.buttons.append(back_button)

        book_icon_name = "icon.png"
        #path = "./audiobooks/*/"
        path = "./"
        path += self.folder
        path += "/*/"
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
