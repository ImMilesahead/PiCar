import os
import sys
import pygame
from Screen import *
from Button import *
from Updater import *
from Variables import *
from pygame.locals import *
from mutagen.id3 import ID3
from datetime import datetime


class MainScreen(Screen):
    def __init__(self, skrn, screenManager, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.screenManager = screenManager
        self.text_color = ((0, 153, 255))
        self.color_theme = (0, 153, 255)
        self.qButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Quit', callback=Quit, text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.text_color)
        self.musicButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Music', callback=self.screenManager.loadScreen, args=1, text_offset=(125, 75), dim=(25, 25, 350, 175), text_color=self.text_color)
        self.updateButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='', callback=Update, text_offset=(10, 30), dim=(680, 240, 100, 100), text_size=36, text_color=self.text_color)
        
        self.diagnosticButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Diagnostics', callback=self.screenManager.loadScreen, args=2, text_offset=(15, 40), dim=(25, 225, 275, 125), text_color=self.text_color)
        self.mapsButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Maps', callback=Nothing, args=None, text_offset=(15, 40), dim=(325, 225, 125, 125), text_color=self.text_color)

        self.timeWindow = Button(skrn=skrn, size=self.size, color=self.color_theme, text='', callback=Nothing, dim=(400, 25, 375, 175))
        self.timeMessage = 'Time Goes Here'
        self.now = datetime.now()
        self.updateImage = pygame.image.load(PICTURES_PATH+'update.png')
        self.updateImage = pygame.transform.scale(self.updateImage, (96, 96))


    def draw(self):
        # Draw background
        self.skrn.fill((35, 35, 35))
        self.skrn.blit(self.updateImage, (680, 242))
        text(self.skrn, self.timeMessage, (450, 85), 96, self.text_color)
        self.timeWindow.draw()
        self.qButton.draw()
        self.updateButton.draw()
        self.musicButton.draw()
        self.diagnosticButton.draw()
        self.mapsButton.draw()

    def logic(self):
        self.now = datetime.now()
        hour = self.now.hour
        minute = self.now.minute


        if minute < 10:
            minute = '0' + str(minute)
        if hour > 12:
            hour = hour - 12
            minute = str(minute) + 'pm'
        else:
            if hour == 0:
                hour = 12
            minute = str(minute) + 'am'
        if hour < 10:
            hour = '0' + str(hour)


        
        self.timeMessage = str(hour) + ':' + str(minute)
        self.timeWindow.logic()
        self.qButton.logic()
        self.updateButton.logic()
        self.musicButton.logic()
        self.diagnosticButton.logic()
        
    def event(self, event):
        self.qButton.event(event)
        self.timeWindow.event(event)
        self.updateButton.event(event)
        self.musicButton.event(event)
        self.diagnosticButton.event(event)
