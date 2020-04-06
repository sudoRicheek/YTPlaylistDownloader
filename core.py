# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:16:37 2020

@author: Richeek Das
"""

from downloadlinks import *

def main():
    url = input("Link to the playlist : ")
    ##Will be downloaded to /cwd/downloads
    playlist_down_obj = downloader(url)
    playlist_down_obj.downloadit()

if __name__=='__main__':
    main()
