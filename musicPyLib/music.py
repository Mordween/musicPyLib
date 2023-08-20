#!/usr/bin/env python3
import pytube
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys

class music:
    def __init__(self):
        #create interface which allow you to choose where dl music
        humanMachineInterface = _HMI()
        self.music_download(humanMachineInterface.playlistURL, humanMachineInterface.musicLocalisation 
                            ,resolution=False, keepOrder=True, playlistPath=humanMachineInterface.playlistLocalisation,
                            playlistName=humanMachineInterface.playlistName)
        

    def music_download(self, URL, musicPath, resolution=False, keepOrder=False, playlistPath=None, playlistName=None):
        playlist = pytube.Playlist(URL)
        if(keepOrder==True):
            if(playlistName==None):
                self.playlistFile = playlistManagement(musicPath, playlist.title, playlistPath)
            else:
                self.playlistFile = playlistManagement(musicPath, playlistName, playlistPath)

        for music in playlist.video_urls:
            yt = pytube.YouTube(music)
            if(resolution==False):
                music = yt.streams.get_audio_only()
            else:
                music = yt.streams.filter(res=resolution, mime_type="video/mp4").first()

            music.download(musicPath)

            if(keepOrder==True):
                print(music.title)
                self.playlistFile.add_song(music.title, '.mp4')

class playlistManagement:
    def __init__(self, songsPath, playlistName, playlistPath):
        playlistPath = 'C:/Users/alexa/Music/MusiquePython/playlist'
        if playlistPath==None :
            self.playlistPath = os.path.join(songsPath, playlistName + '.m3u')
        else:
            self.playlistPath = os.path.join(playlistPath, playlistName + '.m3u')
        self.playlistFile = open(self.playlistPath, 'a')
        self.songsPath = songsPath

    def add_song(self, songName, musicType):
        songFullName = songName.replace("'", "") + musicType
        songPath = os.path.join(self.songsPath, songFullName)
        self.playlistFile.write(songPath + '\n')


    # def playlistPlay(self):
    #     self.playListPath = 'C:/' #TODO make the code in order to read in file text where the playlist is

class _HMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")

        # Créer un widget Entry pour l'URL de la playlist/music
        self.labelPlaylistURL = tk.Label(self.root, text="Playlist URL:")
        self.labelPlaylistURL.pack()
        self.entryPlaylistURL = tk.Entry(self.root)
        self.entryPlaylistURL.pack()

        # Créer un widget Entry pour le nom de la playlist
        self.labelPlaylistName = tk.Label(self.root, text="Playlist name:")
        self.labelPlaylistName.pack()
        self.entryPlaylistName = tk.Entry(self.root)  
        self.entryPlaylistName.pack()

        self.buttonMusicLocalisation = tk.Button(self.root, text="music localisation", command=self.__music_localisation)
        self.buttonMusicLocalisation.pack()

        self.buttonPlaylistLocalisation = tk.Button(self.root, text="playlist localisation", command=self.__playlist_localisation)
        self.buttonPlaylistLocalisation.pack() 

        self.buttonLogin = tk.Button(self.root, text="lancer le téléchargement", command=self.__launch_download)
        self.buttonLogin.pack()
        # Ajout de la possibilité de valider en pressant la touche "Enter" du clavier
        # self.entryPlaylistLocalisation.bind("<Return>", self.__launch_download)

        self.root.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.root.mainloop()

    def __playlist_localisation(self):
        self.entryPlaylistLocalisation = filedialog.askdirectory() 

    def __music_localisation(self):
        self.entryMusicLocalisation = filedialog.askdirectory()

    def __launch_download(self):
        self.playlistURL = self.entryPlaylistURL.get()
        self.playlistName = self.entryPlaylistName.get()
        self.musicLocalisation = self.entryMusicLocalisation
        self.playlistLocalisation = self.entryPlaylistLocalisation
        print(self.playlistURL)
        print(self.playlistName)
        print(self.playlistLocalisation)
        print(self.musicLocalisation)
        self.root.destroy()

    def __onClosing(self):
        """ Trigger when you want to close the Human Machine Interface with the cross
        """
        if messagebox.askyesno("Quitter", "Voulez vous vraiment quitter ?"):
            self.root.destroy()
            sys.exit()


if __name__=='__main__':
    music()
