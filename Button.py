from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from Updater import *
from datetime import datetime
from Functions import *
from Screen import *


pygame.init()
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

def LoadMusic(args):
    args[0].currentScreen = 1

def BackToMenu(args):
    args[0].currentScreen = 0

def PlaySong(args):
    pygame.mixer.music.load(MUSIC_PATH+'\\'+args[0])
    pygame.mixer.music.play()
    print('Playing song at: ' + MUSIC_PATH+args[0])
    args[1].playing = True

def ToggleMusic(args):
    if args[0].playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    args[0].playing = not args[0].playing

def ScrollUp(args):
    musicScreen = args[0]
    musicScreen.start -= 1
    musicScreen.end -= 1
    if musicScreen.start <= 0:
        musicScreen.start = 0
        musicScreen.end = 10

def ScrollDown(args):
    musicScreen = args[0]
    musicScreen.start += 1
    musicScreen.end += 1
    if musicScreen.end >= len(musicScreen.music):
        musicScreen.end = len(musicScreen.music)
        musicScreen.start = musicScreen.end - 10

def PreviousSong(args):
    if args[0].cur_song == 0:
        args[0].cur_song = len(args[0].music)-1
    else:
        args[0].cur_song = args[0].cur_song + 1
    pygame.mixer.load(MUSIC_PATH+'\\'+args[0].music[args[0].cur_song])

def NextSong(args):
    if args[0].cur_song >= len(args[0].music):
        args[0].cur_song = 0
    else:
        args[0].cur_song = args[0].cur_song + 1
    pygame.mixer.music.load(MUSIC_PATH+'\\'+args[0].music[args[0].cur_song])
    pygame.mixer.music.play()

    

def text(skrn, text, pos=(0, 0), size=60, color=(255, 200, 100)):
    sys_font = pygame.font.SysFont("None", int(size))
    rendered = sys_font.render(str(text), 0, color)
    skrn.blit(rendered, pos)


class Button(Screen):
    def __init__(self, skrn, size=(800, 480), dim=(0, 0, 100, 100), color=(255, 0, 0), text='None', text_size=60, text_color=(255, 255, 255), text_offset=(0, 0), callback=Nothing, width=2, args=None):
        Screen.__init__(self, skrn, size)
        self.dim = dim
        self.color = color
        self.text = text
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
        text(skrn, self.text, (self.dim[0] + self.text_offset[0], self.dim[1] + self.text_offset[1]), self.text_size, self.text_color)

    def logic(self):
        '''mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if mouse_pos[0] >= self.dim[0] and mouse_pos[0] <= self.dim[0] + self.dim[2] and mouse_pos[1] >= self.dim[1] and mouse_pos[1] <= self.dim[1] + self.dim[3]:
            if pressed[0]:
               self.callback()'''
        pass

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] >= self.dim[0] and mouse_pos[0] <= self.dim[0] + self.dim[2] and mouse_pos[1] >= self.dim[1] and mouse_pos[1] <= self.dim[1] + self.dim[3]:
                if self.args == None:
                    self.callback()
                else:
                    self.callback(self.args)

