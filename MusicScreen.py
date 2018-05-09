from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from datetime import datetime
from Screen import *
from Button import *
from Song import *
from PlaylistManager import *


class MusicScreen(Screen):
    def __init__(self, skrn, screenManager, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.screenManager = screenManager
        self.playlistManager = PlaylistManager(skrn, screenManager)
        self.playing = False
        self.color_theme = (0, 153, 255)
        
        self.playButton = Button(skrn=skrn, size=self.size, text='>\||', text_size=30, callback=ToggleMusic, args=[self], dim=(100, 410, 50, 50), color=self.color_theme, width=2, text_offset=(15, 5), image='playPause.png')
        self.nextButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Next', text_size=30, callback=NextSong, args=[self], text_offset=(15, 5), dim=(165, 410, 75, 50), width=2, image='next.png')
        self.prevButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Prev', text_size=30, callback=NextSong, args=[self], text_offset=(15, 5), dim=(15, 410, 75, 50), width=0)
        self.backButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=BackToMenu, args=[self.screenManager], text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)
        self.shuffleButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Shuffle', text_size=30, callback=Shuffle, args=[self.playlistManager.playlists[self.playlistManager.currentPlaylist], self.screenManager], text_offset=(15, 5), dim=(250, 410, 65, 50), width=2, image='shuffle.png')


    def draw(self):
        self.skrn.fill((35, 35, 35))
        self.playlistManager.draw()
        self.drawButtons()
        self.backButton.draw()

    def drawButtons(self):
        self.playButton.draw()
        self.nextButton.draw()
        self.prevButton.draw()
        self.shuffleButton.draw()
    
    def logic(self):
        self.playlistManager.logic()
        self.buttonLogic()
        self.backButton.logic()
    def buttonLogic(self):
        self.playButton.logic()
        self.nextButton.logic()
        self.prevButton.logic()
        self.shuffleButton.logic()

    def event(self, event):
        self.playlistManager.event(event)
        self.buttonEvent(event)
        self.backButton.event(event)
    def buttonEvent(self, event):
        self.playButton.event(event)
        self.nextButton.event(event)
        self.prevButton.event(event)
        self.shuffleButton.event(event)
