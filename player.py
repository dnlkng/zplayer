import subprocess
import os


class Player:
    """Wrapper class for mplayer"""

    def playTrack(self, track):
        if self.isPlaying:
            print "terminate"
            self.playerProcess.terminate()

        log_stdin = open("log_stdin.log", "w")
        log_stdout = open("log_stdout.log", "w")
        log_stderr = open("log_stderr.log", "w")
        DNULL = open(os.devnull, "w")
        self._isPlaying = True

        cmd = ["mplayer", track]

        print cmd

        self.playerProcess = subprocess.Popen(cmd,
                                         stdout=log_stdout,
                                         stdin=subprocess.PIPE, 
                                         stderr=log_stderr)    

    def stop(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("q")
        self._isPlaying = False

    def nextInPlaylist(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write(">")

    def previouseInPlaylist(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("<")

    def increaseVolume(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("*")

    def decreaseVolume(self):
        if not hasattr(self, 'playerProcess'):
            return False
        self.playerProcess.stdin.write("/")

    def togglePlayPause(self):
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
    def isPlaying(self):
        if not hasattr(self, 'playerProcess'):
            return False

        if self.playerProcess.poll() is None:
            self._isPlaying = True
        else:
            self._isPlaying = False
        return self._isPlaying

    def __init__(self):
        self._isPlaying = False
        self._isPaused = False
        #self.arg = arg
        pass
