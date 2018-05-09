from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3
from datetime import datetime
from Screen import *
from Button import *
from Song import *
from PlaylistManager import *


class MusicScreen(Screen):
    def __init__(self, skrn, screenManager, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.screenManager = screenManager
        self.playlistManager = PlaylistManager(skrn, screenManager)
        self.playing = False
        self.color_theme = (0, 153, 255)
        
        self.playButton = Button(skrn=skrn, size=self.size, text='>\||', text_size=30, callback=ToggleMusic, args=[self], dim=(100, 420, 50, 30), color=self.color_theme, width=0, text_offset=(15, 5))
        self.nextButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Next', text_size=30, callback=NextSong, args=[self], text_offset=(15, 5), dim=(165, 420, 75, 30), width=0)
        self.prevButton = Button(skrn=skrn, size=self.size, color=self.color_theme, text='Prev', text_size=30, callback=NextSong, args=[self], text_offset=(15, 5), dim=(15, 420, 75, 30), width=0)
        self.backButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=BackToMenu, args=[self.screenManager], text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)


    def draw(self):
        self.skrn.fill((35, 35, 35))
        self.playlistManager.draw()
        self.drawButtons()
        self.backButton.draw()

    def drawButtons(self):
        self.playButton.draw()
        self.nextButton.draw()
        self.prevButton.draw()
    
    def logic(self):
        self.playlistManager.logic()
        self.buttonLogic()
        self.backButton.logic()
    def buttonLogic(self):
        self.playButton.logic()
        self.nextButton.logic()
        self.prevButton.logic()

    def event(self, event):
        self.playlistManager.event(event)
        self.buttonEvent(event)
        self.backButton.event(event)
    def buttonEvent(self, event):
        self.playButton.event(event)
        self.nextButton.event(event)
        self.prevButton.event(event)

'''
class MusicScreen(Screen):
    def __init__(self, skrn, screenManager, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.screenManager = screenManager
        self.music = os.listdir(MUSIC_PATH)
        self.musicNames = []
        for song in self.music:
            realdir = str(os.getcwd()) + MUSIC_PATH + song
            audio = ID3(realdir)
            self.musicNames.append(audio['TIT2'].text[0])
        self.cur_song = 0
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_PATH+'\\'+self.music[self.cur_song])
        self.playing = False
        self.musicButtons = []
        self.start = 0
        self.end = 10
        self.color_theme = (255, 0, 255)
        
        self.bButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=BackToMenu, args=[self.screenManager], text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)
        for x in range(len(self.music)):
            self.musicButtons.append(Button(skrn=self.skrn, size=self.size, dim=(25, 65+x*35, 600, 30), text=self.musicNames[x], callback=PlaySong, args=[self.music[x], self], text_offset=(10, 5), color=self.color_theme, text_size=30, width=0))

        self.sortLabel = Button(skrn=self.skrn, size=self.size, dim=(25, 25, 89, 30), text='Sort by:', callback=Nothing, text_offset=(10, 5), color=self.color_theme, text_size=30, width=0)
        self.songSort = Button(skrn=self.skrn, size=self.size, dim=(25+90, 25, 169, 30), text='Song Name', callback=Nothing, text_offset=(10, 5), color=self.color_theme, text_size=30, width=0)
        self.artSort = Button(skrn=self.skrn, size=self.size, dim=(25+90+170, 25, 169, 30), text='Artist Name', callback=Nothing, text_offset=(10, 5), color=self.color_theme, text_size=30, width=0)
        self.albumSort = Button(skrn=self.skrn, size=self.size, dim=(25+90+170+170, 25, 169, 30), text='Album Name', callback=Nothing, text_offset=(10, 5), color=self.color_theme, text_size=30, width=0)

        self.scrollUp = Button(skrn=self.skrn, size=self.size, text='/\\', text_size=30, callback=ScrollUp, args=[self], dim=(626, 65, 40, 150), color=self.color_theme, width=0, text_offset=(15, 5))
        self.scrollDown = Button(skrn=self.skrn, size=self.size, text='\\/', text_size=30, callback=ScrollDown, args=[self], dim=(626, 260, 40, 150), color=self.color_theme, width=0, text_offset=(15, 130))       
        self.playPause = Button(skrn=skrn, size=self.size, text='>\||', text_size=30, callback=ToggleMusic, args=[self], dim=(100, 420, 50, 30), color=self.color_theme, width=0, text_offset=(15, 5))


    def draw(self):
        #self.skrn.blit(self.bg, (0, 0))
        self.skrn.fill((255, 255, 255))
        self.bButton.draw()
        self.sortLabel.draw()
        self.songSort.draw()
        self.artSort.draw()
        self.albumSort.draw()
        self.scrollUp.draw()
        self.scrollDown.draw()
        self.playPause.draw()
        for x in range(self.start, self.end):
            self.musicButtons[x].draw()
            

    def logic(self):
        self.bButton.logic()
        self.sortLabel.logic()
        self.songSort.logic()
        self.artSort.logic()
        self.albumSort.logic()
        self.scrollUp.logic()
        self.scrollDown.logic()
        self.playPause.logic()
        for x in range(self.start, self.end):

            self.musicButtons[x].set_dim((25, 65+(x-self.start)*35, 600, 30))
            
            self.musicButtons[x].logic()

    def event(self, event):
        self.bButton.event(event)
        self.sortLabel.event(event)
        self.songSort.event(event)
        self.artSort.event(event)
        self.albumSort.event(event)
        self.scrollUp.event(event)
        self.scrollDown.event(event)
        self.playPause.event(event)
        for x in range(self.start, self.end):
            self.musicButtons[x].event(event)
'''