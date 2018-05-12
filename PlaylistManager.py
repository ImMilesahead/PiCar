import os
import sys
import pygame
from Song import *
from Screen import *
from Button import *
from Updater import *
from Playlist import *
from Variables import *
from pygame.locals import *
from mutagen.id3 import ID3
from PlaylistManager import *
from PlaylistDisplay import *
from datetime import datetime


class PlaylistManager(Screen):
    def __init__(self, skrn, screenManager, size=(800, 480)):
        Screen.__init__(self, skrn, size)
        self.playlists = []
        self.loadPlaylists()
        self.playlistDisplay = PlaylistDisplay(skrn, screenManager, self, self.playlists[0])
        self.playlistButtons = []
        self.color_theme = (0, 153, 255)
        for x in range(len(self.playlists)):
            self.playlistButtons.append(Button(skrn=skrn, size=self.size, dim=(25, 65+x*35, 600, 30), text=self.playlists[x].name, callback=self.loadPlaylist, args=x, text_offset=(10, 5), color=self.color_theme, text_size=30, width=0))
        self.currentPlaylist = 0
        self.playingPlaylist = 0
        self.showPlaylist = False
        self.start = 0
        self.end = len(self.playlists)
        if self.end > 10:
            self.end = 10

    def draw(self):
        if self.showPlaylist:
            self.playlistDisplay.draw()
        else:
            for x in range(self.start, self.end):
                self.playlistButtons[x].draw()
    
    def logic(self):
        if self.showPlaylist:
            self.playlistDisplay.logic()
        else:
            for x in range(self.start, self.end):
                self.playlistButtons[x].set_dim((25, 55+(x-self.start)*35, 600, 30))
                self.playlistButtons[x].logic()
    
    def event(self, event):
        if self.showPlaylist:
            self.playlistDisplay.event(event)
        else:
            for x in range(self.start, self.end):
                self.playlistButtons[x].event(event)
    
    def loadPlaylist(self, playlist):
        if not self.showPlaylist:
            self.currentPlaylist = playlist
            self.showPlaylist = True # I think that's how I do it
            #Forgot this part
            self.playlistDisplay.setPlaylist(self.playlists[self.currentPlaylist])
            # Actually do the playing here
            # IDK how to do that
            # Alright yes this works leave it alone
        else:
            #if not self.playing:
            # actually it should never  be called like this so uh yeah this shouldn't ever happen
            pass
    def loadAllSongs(self):
        playlist = open(MEDIA_PATH + 'Playlists/AllSongs', 'w')
        songs = os.listdir(MUSIC_PATH)
        for song in songs:
            playlist.write(song + '\n')
        playlist.close()

    def loadPlaylists(self):
        self.loadAllSongs()
        playlists = os.listdir(MEDIA_PATH+'Playlists/')
        for playlist in playlists:
            plist = Playlist(playlist)
            self.playlists.append(plist)

    def prevSong(self):
        self.playlists[self.playingPlaylist].prevSong()
    def nextSong(self):
        self.playlists[self.playingPlaylist].nextSong()
    def getCurSong(self):
        return self.playlists[self.playingPlaylist].getCurSong()
    def shuffle(self):
        self.playlists[self.playingPlaylist].shuffle()
        self.playlistDisplay.setPlaylist(self.playlists[self.playingPlaylist])
    def getCurrentSongName(self):
        return self.playlists[self.playingPlaylist].getCurrentPlayingSongName()