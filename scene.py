class Scene(object):
    """Abstract Scene"""

    def __init__(self, scene_manager):
        self.manager = scene_manager

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, e):
        raise NotImplementedError
