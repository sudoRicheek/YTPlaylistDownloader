# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:16:37 2020

@author: Richeek Das
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sys
import os

class GetAllPlaylistLinks():

    def __init__(self):
        self.driver = None

    def load_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd() +"/chromedriver"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)    #opens the browser


    def load_url(self, playlist_id):
        url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.driver.get(url)
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "thumbnail")))


    def load_all_vids(self):##needs improvement
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath("//body")).click()

        nlinks = 0
        while True:
            content = self.driver.page_source
            soup = BeautifulSoup(content, 'lxml')
            if(nlinks == len(soup.find_all('a', id="thumbnail", href=True))):
                break
            else:
                nlinks = len(soup.find_all('a', id="thumbnail", href=True))

            for i in range(1,18): ##Takes approximately 18 keydowns to load the next 100 vids
                act.send_keys(Keys.PAGE_DOWN).perform()

            time.sleep(4) ## Sorry bit of hardcoding here :P

    ###Like if you ever need this feature :P
    def get_scrnsht(self):
        self.driver.get_screenshot_as_file("capture.png")

    def get_content(self):
        content = self.driver.page_source
        self.driver.close()
        count = 0
        soup = BeautifulSoup(content, 'lxml')
        links = []
        for element in soup.find_all('a', id="thumbnail", href=True):
            rawlink = element['href']
            if(count >= 1):
                try:
                    str = rawlink[:rawlink.index("&list=")]
                except ValueError :
                    continue

                try :
                    str2 = rawlink[:rawlink.index("&start_radio=")]
                except ValueError :
                    links.append("http://youtube.com/" + str)

            count += 1
        ###Loop ends here
        return links

    def get_link_list(self, playlist_id):
        self.load_driver()
        self.load_url(playlist_id)
        self.load_all_vids()
        finallinks = self.get_content()

        return finallinks
