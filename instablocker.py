from selenium.common.exceptions import NoSuchElementException
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options


class Instablocker():
    def __init__(self):
        opts = Options()
        self.driver = webdriver.Chrome(chrome_options=opts)
    def login(self, username, password)
    instablocker.go_to_target(target)
    while True:
        if instablocker.block(target):
            instablocker.refresh()
            # this set to 6 seconds fails at around 30 minutes
            time.sleep(19)
    else: 
        exit()


