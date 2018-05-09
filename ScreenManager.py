from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from Updater import *
from datetime import datetime
from Screen import *
from Button import *
from MainScreen import *
from MusicScreen import *

class ScreenManager:
    def __init__(self, skrn):
        self.skrn = skrn
        self.screens = [MainScreen(skrn, self), MusicScreen(skrn, self)]
        self.currentScreen = 0
        self.mouse_pos = (0, 0)
        self.systemMessage = 'All Systems Green!'
    
    def update(self):
        self.skrn.fill((0, 0, 0))
        self.screens[self.currentScreen].draw()
        text(self.skrn, self.mouse_pos, (10, 462), 24, (255, 255, 255))
        text(self.skrn, self.systemMessage, (650, 462), 24, (0, 255, 0))
        self.screens[self.currentScreen].logic()
        if not pygame.mixer.music.get_busy() and self.screens[1].playing:
            NextSong([self.screens[1]])
        # Mouse Logic
        mouse_pos = pygame.mouse.get_pos()
    def event(self, event):
        self.screens[self.currentScreen].event(event)
        
