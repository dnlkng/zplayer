from filebrowserscene import FileBrowserScene
from playerscene import PlayerScene
from mainmenu import MainMenuScene


class SceneManager(object):

    def __init__(self):
        self.current_scene = None
        # self.menu_scene = MenuScene(self)
        self.main_menu_scene = MainMenuScene(self)
        self.file_browser_scene = FileBrowserScene(self)
        self.player_scene = PlayerScene(self)
        self.go_to(self.main_menu_scene)

    def go_to(self, scene):
        self.current_scene = scene

    def show_main_menu(self):
        self.main_menu_scene.has_updates = True
        self.go_to(self.main_menu_scene)

    def show_player(self, folder, is_for_music):
        self.player_scene.set_folder(folder, is_for_music)
        self.go_to(self.player_scene)

    def show_filebrowser(self, folder, is_for_music):
        self.file_browser_scene.set_folder(folder, is_for_music)
        self.go_to(self.file_browser_scene)
