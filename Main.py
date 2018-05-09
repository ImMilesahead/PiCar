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
from ScreenManager import *

class PlaylistManager:
    def __init__(self):
        self.playlists = []
        self.size = 0
        self.currentPlaylist = 0 



if __name__ == '__main__':

    screenManager = ScreenManager(skrn)

    pygame.display.set_caption(name)

    while True:

        screenManager.update()
        pygame.display.flip()
        ''' Events '''
        for event in pygame.event.get():
            screenManager.event(event)
