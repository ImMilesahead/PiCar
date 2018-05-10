from Variables import *
import sys
import os
from mutagen.id3 import ID3
from Song import *
from random import shuffle
from Button import *

class Playlist:
    def __init__(self, listFile=None):
        self.name = listFile
        self.isPlaying = False
        self.currentlyPlaying = 0
        self.songs = []
        self.size = 0
        self.loadPlaylist()
        '''
        playlist length hours
        '''
    def loadPlaylist(self):
        playlistFile = open('./Media/Playlists/' + self.name, 'r')
        lines = playlistFile.read().split('\n')
        playlistFile.close()
        for line in lines:
            if len(line) < 2:
                break
            realdir = str(os.getcwd()) + '/' + MUSIC_PATH + line
            audio = ID3(realdir)
            name = audio['TIT2'].text[0]
            self.songs.append(Song(name, line))
        self.size = len(self.songs)

    def addSong(self, songPath):
        playlistFile = open('./Media/Playlists/' + self.name, 'a')
        playlistFile.write(songPath + '\n')
        playlistFile.close()
        self.size = len(self.songs)

    def removeSong(self, songPath):
        playlistFile = open('./Media/Playlists/' + self.name, 'r')
        lines = playlistFile.read().split('\n')
        playlistFile.close()
        playlistFile = open('./Media/Playlists/' + self.name, 'w')
        for line in lines:
            if not line == songPath:
                playlistFile.write(line + '\n')
        playlistFile.close()
        self.size = len(self.songs)

    def sortByName(self, reverse=False):
        if not reverse:
            for x in range(self.size-1):
                for y in range(x, self.size):
                    if self.songs[x].name > self.songs[y].name:
                        dummy = self.songs[x]
                        self.songs[x] = self.songs[y]
                        self.songs[y] = dummy
        else:
            for x in range(self.size-1):
                for y in range(x, self.size):
                    if self.songs[x].name > self.songs[y].name:
                        dummy = self.songs[x]
                        self.songs[x] = self.songs[y]
                        self.songs[y] = dummy
    def sortByArtist(self, reverse=False):
        if not reverse:
            for x in range(self.size-1):
                for y in range(x, self.size):
                    if self.songs[x].artist > self.songs[y].artist:
                        dummy = self.songs[x]
                        self.songs[x] = self.songs[y]
                        self.songs[y] = dummy
        else:
            for x in range(self.size-1):
                for y in range(x, self.size):
                    if self.songs[x].artist > self.songs[y].artist:
                        dummy = self.songs[x]
                        self.songs[x] = self.songs[y]
                        self.songs[y] = dummy
    def nextSong(self):
        if self.currentlyPlaying < self.size-1:
            self.currentlyPlaying = self.currentlyPlaying + 1
        else:
            self.currentlyPlaying = 0
        
    def prevSong(self):
        if self.currentlyPlaying > 0:
            self.currentlyPlaying = self.currentlyPlaying - 1
        else:
            self.currentlyPlaying = self.size-1
    def getCurSong(self):
        path = self.songs[self.currentlyPlaying].path
        return path
        
    def shuffle(self):
        shuffle(self.songs)
        
    def playSong(self, song):
        self.currentlyPlaying = song
        pygame.mixer.music.load(MUSIC_PATH+'\\'+ self.getCurSong())
        pygame.mixer.music.play()