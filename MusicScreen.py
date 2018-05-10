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
        
        self.playButton = Button(skrn=skrn, size=self.size, text='>\||', text_size=30, callback=self.toggleMusic, args=None, dim=(125, 385, 75, 75), color=self.color_theme, width=2, text_offset=(15, 5), image='playPause.png', image_offscale=(20, 20), image_offset=(10, 10))
        self.nextButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Next', text_size=30, callback=self.nextSong, args=None, text_offset=(15, 5), dim=(225, 385, 75, 75), width=2, image='next.png', image_offscale=(20, 20), image_offset=(10, 10))
        self.prevButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Prev', text_size=30, callback=self.prevSong, args=None, text_offset=(15, 5), dim=(25, 385, 75, 75), width=2, image='prev.png', image_offset=(10, 10), image_offscale=(20, 20))
        self.backButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=self.back, args=None, text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)


    def draw(self):
        self.skrn.fill((35, 35, 35))
        self.playlistManager.draw()
        self.drawButtons()
        self.backButton.draw()

    def drawButtons(self):
        self.playButton.draw()
        self.nextButton.draw()
        self.prevButton.draw()
        #self.shuffleButton.draw()
    
    def logic(self):
        self.playlistManager.logic()
        self.buttonLogic()
        self.backButton.logic()
    def buttonLogic(self):
        self.playButton.logic()
        self.nextButton.logic()
        self.prevButton.logic()
        #self.shuffleButton.logic()

    def event(self, event):
        self.playlistManager.event(event)
        self.buttonEvent(event)
        self.backButton.event(event)
    def buttonEvent(self, event):
        self.playButton.event(event)
        self.nextButton.event(event)
        self.prevButton.event(event)
        #self.shuffleButton.event(event)

    def nextSong(self):
        self.playlistManager.nextSong()
        self.playing = True
        pygame.mixer.music.load(MUSIC_PATH+'/'+str(self.playlistManager.getCurSong()))
        pygame.mixer.music.play()

    def prevSong(self):
        self.playlistManager.prevSong()
        pygame.mixer.music.load(MUSIC_PATH+'/'+str(self.playlistManager.getCurSong()))
        pygame.mixer.music.play()

    def back(self):
        if self.playlistManager.showPlaylist:
            self.playlistManager.showPlaylist = False
        else:
            self.screenManager.loadScreen(0)

    
    def toggleMusic(self):
        if self.playing:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.playing = not self.playing

    def shuffle(self):
        self.playlistManager.shuffle()