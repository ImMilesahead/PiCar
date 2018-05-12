import os
import sys
import pygame
from Updater import *
from Variables import *
from pygame.locals import *
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from datetime import datetime


class Song:
    def __init__(self, path):
        self.path = path
        self.name = "None"
        try:
            audio = MP3(self.getRealPath())
            self.length = audio.info.length
            audio = ID3(self.getRealPath())
            self.name = audio['TIT2'].text[0]
            self.artist = audio['TPE1'].text[0]
            self.album = audio['TALB'].text[0]
            self.genre = audio['TCON'].text[0]
            self.releaseYear = audio['TDRC'].text[0]
        except:
            print ('Something went wrong')
            print(self.path)
    def getRealPath(self):
        return MUSIC_PATH + self.path