import pygame
from pygame import *
from button import Button
from scene import Scene
import globals


class MainMenuScene(Scene):
    """Main Menu scene"""

    def __init__(self, scene_manager):
        super(MainMenuScene, self).__init__(scene_manager)
        self.bg = Surface(globals.SCREEN_SIZE)
        self.bg.fill(Color("#fdf6e3"))

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
        is_for_music = False
        if folder is "music":
            is_for_music = True

        self.manager.show_filebrowser(folder, is_for_music)

    def build_menu(self):
        music_button = Button((60, 80, 80, 80), value="music", cb=self.on_button_clicked)
        music_button.iconFg = pygame.image.load("./resources/images/note.png")
        book_button = Button((180, 80, 80, 80), value="audiobooks", cb=self.on_button_clicked)
        book_button.iconFg = pygame.image.load("./resources/images/book.png")

        self.buttons.append(music_button)
        self.buttons.append(book_button)

