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

password):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1) 
        username_elem = driver.find_element_by_name("username")
        username_elem.clear()
        username_elem.send_keys(username)
        password_elem = driver.find_element_by_name("password")
        password_elem.clear()
        password_elem.send_keys(password)
        time.sleep(1) 
        password_elem.send_keys(Keys.RETURN)
        time.sleep(3) # Adjust according to your Internet speed
        continue_link = driver.find_element_by_xpath("//button[contains(.,'Not Now')]")
        continue_link.click()
    
    def go_to_target(self, target):
        driver = self.driver
        driver.get("https://www.instagram.com/" + target + "/")
        

    def block(self, target):
        driver = self.driver
        
        try:
            #Check if sorry profile missing message. If fails then block
            if driver.find_element_by_xpath("/html/body/div/div[1]/div/div/h2"):
                return True
        except NoSuchElementException: 
            time.sleep(3)
            print("exception happened")
            #Click Sprite drop down
            element = driver.find_element_by_xpath("//button[@class='dCJp8 afkep']")
            element.send_keys(Keys.ENTER)
            # Press block button
            block_button = driver.find_element_by_xpath("//button[contains(.,'Block this user')]")
            block_button.send_keys(Keys.ENTER)
            #Confirm block
            confirm_button = driver.find_element_by_xpath("//button[contains(.,'Block')]")
            confirm_button.send_keys(Keys.ENTER)
            
            now = datetime.now()
            current_time = now.strftime("%d/%m/%y %H:%M:%S")
            print(" Target @" + target + " BLOCKED TIME:" + current_time)
            
            exit()
    def refresh(self):
        driver = self.driver
        driver.refresh()
    

    instablocker.go_to_target(target)
    while True:
        if instablocker.block(target):
            instablocker.refresh()
            # this set to 6 seconds fails at around 30 minutes
            time.sleep(19)
    else: 
        exit()

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




