# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:16:37 2020

@author: Richeek Das
"""

from getlinklist import *
from pytube import YouTube
import os
import time

class downloader():

    def __init__(self, playlist_id):
        playlist_info = GetAllPlaylistLinks()
        self.linklist = playlist_info.get_link_list(playlist_id)

    def downloadStuff(self):
        """
        For now it has been defaulted to the highest available quality
        """
        path = os.getcwd() +"/downloads"
        for link in self.linklist:
            yt = YouTube(link)
            time.sleep(3)
            #path = os.getcwd() +"/downloads"
            yt.streams.first().download(path)
            print("Download Complete : " + yt.title)


    def downloadit(self):
        self.downloadStuff()
