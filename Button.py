from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from Updater import *
from datetime import datetime
from Screen import *


pygame.init()
pygame.mixer.init()
     
skrn = pygame.display.set_mode((800, 480))

def Nothing():
    pass

def Update():
    global SystemMessage
    if update():
        SystemMessage = 'Update Ready'
    else:
        SystemMessage = 'No Updates Found'

def Quit():
    pygame.quit()
    sys.exit()

def text(skrn, text, pos=(0, 0), size=60, color=(255, 200, 100)):
    sys_font = pygame.font.SysFont("None", int(size))
    rendered = sys_font.render(str(text), 0, color)
    skrn.blit(rendered, pos)


class Button(Screen):
    def __init__(self, skrn, size=(800, 480), dim=(0, 0, 100, 100), color=(0, 153, 255), text='None', text_size=60, text_color=(255, 255, 255), text_offset=(0, 0), callback=Nothing, width=2, args=None, image=None, image_offset=(3, 3), image_offscale=(6, 6)):
        Screen.__init__(self, skrn, size)
        self.dim = dim
        self.color = color
        self.text = text
        self.image = image
        self.image_offset= image_offset
        self.image_offscale = image_offscale
        if not image == None:
            self.image = pygame.image.load(PICTURES_PATH + image)
            self.image = pygame.transform.scale(self.image, (self.dim[2]-self.image_offscale[0], self.dim[3]-self.image_offscale[1]))
        self.text_size = text_size
        self.text_color = text_color
        self.text_offset = text_offset
        self.callback = callback
        self.width = width
        self.args=args

    def set_dim(self, dim):
        self.dim = dim
    
    def draw(self):
        pygame.draw.rect(self.skrn, self.color, self.dim, self.width)
        # draw text
        if not self.image == None:
            self.skrn.blit(self.image, (self.dim[0]+self.image_offset[0], self.dim[1]+self.image_offset[1]))
        else:
            text(skrn, self.text, (self.dim[0] + self.text_offset[0], self.dim[1] + self.text_offset[1]), self.text_size, self.text_color)

    def logic(self):
        '''mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if mouse_pos[0] >= self.dim[0] and mouse_pos[0] <= self.dim[0] + self.dim[2] and mouse_pos[1] >= self.dim[1] and mouse_pos[1] <= self.dim[1] + self.dim[3]:
            if pressed[0]:
               self.callback()'''
        pass

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            self.start_mouse_pos = mouse_pos
            if mouse_pos[0] >= self.dim[0] and mouse_pos[0] <= self.dim[0] + self.dim[2] and mouse_pos[1] >= self.dim[1] and mouse_pos[1] <= self.dim[1] + self.dim[3]:
                if self.args == None:
                    self.callback()
                else:
                    self.callback(self.args)

