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
from MusicScreen import *
from MainScreen import *

class ScreenManager:
    def __init__(self, skrn):
        self.skrn = skrn
        self.screens = []
        self.currentScreen = 0
        self.mouse_pos = (0, 0)
        self.systemMessage = 'All Systems Green!'
    
    def addScreen(self, screen):
        self.screens.append(screen)

    def update(self):
        self.skrn.fill((0, 0, 0))
        self.screens[self.currentScreen].logic()
        self.screens[self.currentScreen].draw()
        text(self.skrn, self.mouse_pos, (10, 462), 24, (255, 255, 255))
        text(self.skrn, self.systemMessage, (650, 462), 24, (0, 255, 0))
        if not pygame.mixer.music.get_busy() and self.screens[1].playing:
            self.screens[1].nextSong()
        # Mouse Logic
        self.mouse_pos = pygame.mouse.get_pos()
        if not self.currentScreen == 1:
            self.screens[1].drawButtons()
            self.screens[1].buttonLogic()
    def event(self, event):
        self.screens[self.currentScreen].event(event)
        if not self.currentScreen == 1:
            self.screens[1].buttonEvent(event)
    def loadScreen(self, x):
        self.currentScreen = x