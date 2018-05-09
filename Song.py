from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from Updater import *
from datetime import datetime

class Song:
    def __init__(self, name, path, artist=None):
        self.name = name
        self.path = path
        self.artist = artist
        '''
        song length seconds
        '''
    def getRealPath(self):
        return MUSIC_PATH + self.path