from Playlist import *
import pygame
from pygame.locals import *
from ScreenManager import *
from Button import *

class PlaylistDisplay(Screen):
    def __init__(self, skrn, screenManager, playlistManager, playlist, size=(800, 480)):
        self.playlist = playlist #Of typer Playlist
        self.skrn = skrn
        self.playlistManager = playlistManager
        self.screenManager = screenManager
        self.size = size
        self.offset = 0
        self.color_theme = (0, 153, 255)
        if playlist == None:
            self.name = None
        else:
            self.name = playlist.name
        self.start = 0
        self.end = 9
        if self.end > self.playlist.size:
            self.end = self.playlist.size-1
        self.setPlaylist(self.playlist)

        self.shuffleButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Shuffle play', text_size=30, callback=self.shuffle, args=None, text_offset=(15, 15), dim=(475, 5, 145, 45), width=2)

        self.upButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Up', text_size=30, callback=self.scrollUp, args=None, text_offset=(15, 15), dim=(650, 55, 100, 100))
        self.downButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Down', text_size=30, callback=self.scrollDown, args=None, text_offset=(15, 15), dim=(650, 200, 100, 100))

    def draw(self):
        # Draw label at top saying name of playlist
        text(skrn, self.name, (25, 15), 48, (255, 255, 255))
        self.shuffleButton.draw()
        # List all songs in playlist
        for x in range(self.start, self.end):
            self.buttons[x].draw()
        self.upButton.draw()
        self.downButton.draw()
        pass

    def logic(self):
        for x in range(self.start, self.end):
            self.buttons[x].set_dim((25, 55+(x-self.start)*35, 600, 30))
            self.buttons[x].logic()
        self.shuffleButton.logic()
        self.upButton.logic()
        self.downButton.logic()
        self.end = self.start + 9
        if self.end > self.size:
            self.end = self.size
    
    def event(self, event):
        for x in range(self.start, self.end):
            self.buttons[x].event(event)
        self.shuffleButton.event(event)
        self.upButton.event(event)
        self.downButton.event(event)

    def setPlaylist(self, playlist):
        self.playlist = playlist
        self.name = self.playlist.name
        self.size = self.playlist.size
        # (Re)load buttons
        self.buttons = []
        
        for x in range(self.playlist.size):
            name = self.playlist.songs[x].name
            if len(name) > 40:
                name = name[0:40] + '...'
            buttonDim = (25, 65 + x*35, 600, 30)
            self.buttons.append(Button(skrn=skrn, size=self.size, dim=buttonDim, text=name, callback=self.playSong, args=x, text_offset=(10, 5), color=self.color_theme, text_color=self.color_theme, text_size=30, width=2))
        
        self.start = 0
        self.end = 9
        if self.end > self.size:
            self.end = self.size

    def scrollUp(self):
        if self.size > 9:
            if self.start > 0:
                self.start = self.start - 1
                self.end = self.start + 9
        else:
            self.start = 0
            self.end = self.size
    def scrollDown(self):
        if self.size > 9:
            if self.start < self.size - 9:
                self.start = self.start + 1
                self.end = self.start + 9

    def shuffle(self):
        self.screenManager.screens[1].shuffle()

    def playSong(self, song):
        self.playlist.playSong(song)
        self.playing = True