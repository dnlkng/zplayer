import subprocess
import os


class Player:
    """Wrapper class for mplayer"""

    def play_track(self, track):
        if self.is_playing:
            print "terminate"
            self.playerProcess.terminate()

        dev_null = open(os.devnull, "w")
        self._isPlaying = True

        cmd = ["mplayer", track]
        self.playerProcess = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    def stop(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("q")
        self._isPlaying = False

    def next_in_playlist(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write(">")

    def previous_in_playlist(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("<")

    def increase_volume(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("*")

    def decrease_volume(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("/")

    def toggle_play_pause(self):
        print "in togglePlayPause"
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("p")
        self._isPaused = not self._isPaused
        print "player.isPaused: ", self._isPaused
        return self._isPaused

    def read(self):
        print self.playerProcess

    @property
    def is_playing(self):
        if not hasattr(self, 'playerProcess'):
            return False

        if self.playerProcess is None:
            return False
        
        if self.playerProcess.poll() is None:
            self._isPlaying = True
        else:
            self._isPlaying = False
        return self._isPlaying

    def __init__(self):
        self._isPlaying = False
        self._isPaused = False
        self.playerProcess = None
        pass
