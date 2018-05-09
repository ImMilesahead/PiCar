from Playlist import *
import pygame
from pygame.locals import *
from ScreenManager import *
from Button import *

class PlaylistDisplay(Screen):
    def __init__(self, skrn, screenManager, playlist, size=(800, 480)):
        self.playlist = playlist #Of typer Playlist
        self.skrn = skrn
        self.screenManager = screenManager
        self.size = size
        self.offset = 0
        self.color_theme = (0, 153, 255)
        if playlist == None:
            self.name = None
        else:
            self.name = playlist.name
        self.start = 0
        self.end = 10
        if self.end > self.playlist.size:
            self.end = self.playlist.size-1
        self.setPlaylist(self.playlist)

    def draw(self):
        # Draw label at top saying name of playlist
        
        for x in range(self.start, self.end):
            self.buttons[x].draw()
        # List all songs in playlist
        pass

    def logic(self):
        for x in range(self.start, self.end):
            self.buttons[x].set_dim((25, 65+(x-self.start)*35, 600, 30))
            self.buttons[x].logic()
    
    def event(self, event):
        for x in range(self.start, self.end):
            self.buttons[x].event(event)

    def setPlaylist(self, playlist):
        self.playlist = playlist
        self.name = self.playlist.name
        # (Re)load buttons
        self.buttons = []
        for x in range(self.playlist.size):
            self.buttons.append(Button(skrn=skrn, size=self.size, dim=(25, 65+x*35, 600, 30), text=self.playlist.songs[x].name, callback=PlaySong, args=[self.playlist.songs[x].path, self], text_offset=(10, 5), color=self.color_theme, text_size=30, width=0))

