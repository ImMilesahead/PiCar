import os
import sys
from Button import *
from Screen import *

class DiagnosticScreen(Screen):
    def __init__(self, skrn, screenManager):
        Screen.__init__(self, skrn, (800, 480))
        self.screenManager = screenManager
        self.color_theme = (0, 153, 255)
        self.backButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=self.screenManager.loadScreen, args=0, text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)


    def draw(self):
        self.skrn.fill((35, 35, 35))
        self.backButton.draw()
    
    def logic(self):
        self.backButton.logic()
    
    def event(self, event):
        self.backButton.event(event)