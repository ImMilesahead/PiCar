from Variables import *
import pygame
from pygame.locals import *
import sys
import os
from mutagen.id3 import ID3

def Quit():
    pygame.quit()
    sys.exit()

def LoadMusic():
    global currentScreen
    currentScreen = 1

def BackToMenu():
    global currentScreen
    currentScreen = 0

def Nothing():
    pass

def PlaySong(args):
    pygame.mixer.music.load(MUSIC_PATH+'\\'+args[0])
    pygame.mixer.music.play()
    print('Playing song at: ' + MUSIC_PATH+args[0])

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
    
class Object:
    def __init__(self, skrn, size=(800, 480)):
        self.skrn = skrn
        self.size = size
    def draw(self):
        pass
    def logic(self):
        pass
    def event(self, event):
        pass

class Button(Object):
    def __init__(self, skrn, size=(800, 480), dim=(0, 0, 100, 100), color=(255, 0, 0), text='None', text_size=60, text_color=(255, 255, 255), text_offset=(0, 0), callback=Quit, width=2, args=None):
        Object.__init__(self, skrn, size)
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

class MainScreen(Screen):
    def __init__(self, skrn, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.qButton = Button(skrn=self.skrn, size=self.size, color=(0, 255, 0), text='Quit', callback=Quit, text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50)
        self.bg = pygame.image.load(PICTURES_PATH+BACKGROUNDS['Main'])
        self.musicButton = Button(skrn=skrn, size=self.size, color=(0, 255, 0), text='Music', callback=LoadMusic, text_offset=(125, 75), dim=(25, 25, 350, 190))
    def draw(self):
        # Draw background
        self.skrn.blit(self.bg, (0, 0))
        self.qButton.draw()
        self.musicButton.draw()

    def logic(self):
        self.qButton.logic()
        self.musicButton.logic()
        
    def event(self, event):
        self.qButton.event(event)
        self.musicButton.event(event)

class MusicScreen(Screen):
    def __init__(self, skrn, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.bg = pygame.image.load(PICTURES_PATH+BACKGROUNDS['Music'])
        self.music = os.listdir(MUSIC_PATH)
        self.musicNames = []
        for song in self.music:
            realdir = str(os.getcwd()) + MUSIC_PATH + song
            audio = ID3(realdir)
            self.musicNames.append(audio['TIT2'].text[0])
        print(self.musicNames)
        self.cur_song = 0
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_PATH+'\\'+self.music[self.cur_song])
        pygame.mixer.music.play()
        self.playing = True
        self.musicButtons = []
        self.start = 0
        self.end = 10
        self.color_theme = (255, 0, 255)
        
        self.bButton = Button(skrn=self.skrn, size=self.size, color=self.color_theme, text='Back', callback=BackToMenu, text_offset=(10, 30), dim=(680, 350, 100, 100), text_size=50, text_color=self.color_theme, width=5)
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
        self.skrn.blit(self.bg, (0, 0))
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
    
def text(skrn, text, pos=(0, 0), size=60, color=(255, 200, 100)):
    sys_font = pygame.font.SysFont("None", int(size))
    rendered = sys_font.render(str(text), 0, color)
    skrn.blit(rendered, pos)



mouse_pos = (0, 0)

SystemMessage = 'All Systems Green'
pygame.init()

skrn = pygame.display.set_mode((800, 480))

pygame.display.set_caption('karu')

skrn.fill((0, 0, 0))

Screens = [MainScreen(skrn),
           MusicScreen(skrn)]

currentScreen = 0

while True:

    skrn.fill((0, 0, 0))
    
    ''' Logic '''
    Screens[currentScreen].logic()
    Screens[currentScreen].draw()
    
    text(skrn, mouse_pos, (10, 462), 24, (255, 255, 255))
    text(skrn, SystemMessage, (650, 462), 24, (0, 255, 0))
    
    if not pygame.mixer.music.get_busy() and Screens[1].playing:
        print('Test')
        NextSong([Screens[1]])

    # Mouse Logic
    mouse_pos = pygame.mouse.get_pos()

    pygame.display.flip()
    ''' Events '''
    for event in pygame.event.get():
        Screens[currentScreen].event(event)

    
