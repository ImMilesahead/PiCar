from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from Updater import *
from datetime import datetime

class Screen:
    def __init__(self, skrn, size=(800, 480)):
        self.skrn = skrn
        self.size = size
    def draw(self):
        pass
    def logic(self):
        pass
    def event(self, event):
        pass