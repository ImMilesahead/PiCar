import os
import sys
import pygame
from Screen import *
from Button import *
from Updater import *
from Variables import *
from MainScreen import *
from MusicScreen import *
from ScreenManager import *
from pygame.locals import *
from mutagen.id3 import ID3
from PlaylistDisplay import *
from datetime import datetime
from DiagnosticScreen import *

if __name__ == '__main__':

    screenManager = ScreenManager(skrn)
    screenManager.addScreen(MainScreen(skrn, screenManager))
    screenManager.addScreen(MusicScreen(skrn, screenManager))
    screenManager.addScreen(DiagnosticScreen(skrn, screenManager))

    pygame.display.set_caption(name)

    while True:

        screenManager.update()
        pygame.display.flip()
        ''' Events '''
        for event in pygame.event.get():
            screenManager.event(event)
