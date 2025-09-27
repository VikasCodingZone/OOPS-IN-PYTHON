# Q11. Music Player (Spotify vs YouTube Music)

# Logic: Music players ek hi kaam karte hain (play), but implementation alag.

from abc import ABC, abstractmethod

class MusicPlayer(ABC):
    @abstractmethod
    def play(self, song):
        pass

class Spotify(MusicPlayer):
    def play(self, song):
        return f"Playing {song} on Spotify "

class YouTubeMusic(MusicPlayer):
    def play(self, song):
        return f"Playing {song} on YouTube Music "

m = Spotify()
print(m.play("Shape of You"))


# Q11. Music Player (Spotify vs YouTube Music)
# Common kaam: song play karna.
# Spotify aur YT Music dono ka backend alag hota hai (APIs).
# User ke liye bas play(song) button available hai.