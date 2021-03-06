import pygame
from pygame import *
from button import Button
from player import Player
from scene import Scene
import globals
import glob
import os


class PlayerScene(Scene):
    """Player scene"""

    def __init__(self, manager_scene):
        super(PlayerScene, self).__init__(manager_scene)
        self.bg = Surface(globals.SCREEN_SIZE)
        self.bg.fill(Color("#fdf6e3"))
        self.font = pygame.font.SysFont('Arial', 64)
        self.text = self.font.render("Next", True, (211, 54, 130))

        self.buttons = []
        self.repeat_button = None
        self.is_repeat_on = False
        self.folder = None
        self.cover_placeholder = "./resources/images/cover_placeholder.jpg"
        self.tracks = []
        self.covers = []
        self.track_count = 0

        self.current_track_index = 0
        self.current_track = None
        self.current_cover = None

        self.is_for_music = False
        self.repeat_empty_icon = "./resources/images/repeat_empty.png"
        self.repeat_full_icon = "./resources/images/repeat_full.png"
        self.player = Player()
        self.is_paused = True

        self.play_pause_button = None
        self.play_icon_file = "./resources/images/play.png"
        self.pause_icon_file = "./resources/images/pause.png"
        self.play_icon = pygame.image.load(self.play_icon_file)
        self.pause_icon = pygame.image.load(self.pause_icon_file)

        self.has_updates = True
        self.init_buttons()

    def render(self, screen):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.text, (2, 5))

        self.current_cover = self.covers[self.current_track_index]
        cover = pygame.image.load(self.current_cover)
        cover = aspect_scale(cover)

        black = (0, 0, 0)
        screen.fill(black)

        rect = cover.get_rect()
        rect.x = 40
        screen.blit(cover, rect)

        for btn in self.buttons:
            btn.draw(screen)

        if self.is_for_music:
            self.repeat_button.draw(screen)

    def update(self):
        if self.is_for_music:
            if self.player.is_playing is False and self.is_paused is False:
                print "track", self.tracks[self.current_track_index], "finished: Play next"
                # self.is_paused = True
                self.has_updates = True
                print "ff"
                if not self.is_repeat_on:
                    if self.current_track_index < self.track_count - 1:
                        self.current_track_index += 1
                    else:
                        self.current_track_index = 0

                self.player.stop()
                self.player.play_track(self.tracks[self.current_track_index])
        else:
            if self.player.is_playing is False and self.is_paused is False:
                print "track", self.tracks[self.current_track_index], "finished"
                self.is_paused = True
                self.play_pause_button.iconFg = self.play_icon
                self.has_updates = True

        current_update_stat = self.has_updates
        self.has_updates = False
        return current_update_stat

    def handle_events(self, e):
        if e.type is pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for btn in self.buttons:
                btn.selected(pos)
            if self.is_for_music:
                self.repeat_button.selected(pos)

    def set_folder(self, folder, is_for_music):
        self.player.stop()
        self.folder = folder
        self.is_for_music = is_for_music
        self.update_data()

    def update_data(self):
        self.has_updates = True
        self.current_track_index = 0
        self.tracks = glob.glob(self.folder + "*.mp3")
        self.tracks.sort()
        self.track_count = len(self.tracks)

        self.covers = []
        for track in self.tracks:
            self.covers.append(
                    track.replace("mp3", "jpg") if os.path.isfile(
                        track.replace("mp3", "jpg")) else self.cover_placeholder)

    def go_to_menu(self):
        self.manager.show_main_menu()

    def repeat(self):
        self.has_updates = True
        print("repeat")
        print(self.is_repeat_on)
        self.is_repeat_on = not self.is_repeat_on

        if self.is_repeat_on:
            self.repeat_button.iconFg = pygame.image.load(self.repeat_full_icon)
        else:
            self.repeat_button.iconFg = pygame.image.load(self.repeat_empty_icon)

    def fast_forward(self):
        self.has_updates = True
        print "ff"
        if self.current_track_index < self.track_count - 1:
            self.current_track_index += 1
        else:
            self.current_track_index = 0

        if not self.is_paused and self.player.is_playing:
            self.player.stop()
            self.player.play_track(self.tracks[self.current_track_index])
        else:
            self.player.stop()

    def rewind(self):
        self.has_updates = True
        print "rewind"
        if self.current_track_index > 0:
            self.current_track_index -= 1
        else:
            self.current_track_index = self.track_count - 1

        if not self.is_paused and self.player.is_playing:
            self.player.stop()
            self.player.play_track(self.tracks[self.current_track_index])
        else:
            self.player.stop()

    def play_pause(self):
        self.has_updates = True
        print "play pause"
        print self.tracks[self.current_track_index]

        if not self.player.is_playing:
            self.play_pause_button.iconFg = self.pause_icon
            self.is_paused = False
            self.player.play_track(self.tracks[self.current_track_index])
        else:
            if self.is_paused:
                self.play_pause_button.iconFg = self.pause_icon
                self.is_paused = False
            else:
                self.play_pause_button.iconFg = self.play_icon
                self.is_paused = True
            self.player.toggle_play_pause()

    def init_buttons(self):
        button = Button((0, 0, 42, 42), cb=self.go_to_menu)
        button.iconFg = pygame.image.load("./resources/images/chevron.png")
        self.buttons.append(button)

        fast_forward = Button((256, 150, 64, 64), cb=self.fast_forward)
        ff_icon = "./resources/images/next.png"
        fast_forward.iconFg = pygame.image.load(ff_icon)
        self.buttons.append(fast_forward)

        self.play_pause_button = Button((128, 150, 64, 64), cb=self.play_pause)
        self.play_pause_button.iconFg = self.play_icon
        self.buttons.append(self.play_pause_button)

        rewind_button = Button((0, 150, 64, 64), cb=self.rewind)
        rewind_icon = "./resources/images/previous.png"
        rewind_button.iconFg = pygame.image.load(rewind_icon)
        self.buttons.append(rewind_button)

        # repeat button for music mode
        self.repeat_button = Button((256, 60, 64, 64), cb=self.repeat)
        self.repeat_button.iconFg = pygame.image.load(self.repeat_empty_icon)


def aspect_scale(img):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    (bx, by) = globals.SCREEN_SIZE
    ix, iy = img.get_size()

    if ix > iy:
        # fit to width
        scale_factor = bx / float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by / float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by / float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx / float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (int(sx), int(sy)))
