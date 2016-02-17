from menuscene import MenuScene
from playerscene import PlayerScene


class SceneManager(object):

    def __init__(self):
        self.current_scene = None
        self.menu_scene = MenuScene(self)
        self.player_scene = PlayerScene(self)
        self.go_to(self.menu_scene)

    def go_to(self, scene):
        self.current_scene = scene

    def show_menu(self):
        self.go_to(self.menu_scene)

    def show_player(self, folder):
        self.player_scene.set_folder(folder)
        self.go_to(self.player_scene)
