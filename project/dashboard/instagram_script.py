from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Selenium2Library
import time
import random
import sys


REALUSER = False
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()


    def closeBrowser(self):
        self.driver.close()

    def login(self):
        aDrive = self.driver
        message = ''
        redirectURL = 'https://www.instagram.com/'

        print("Logging In")
        driver = self.driver
        driver.get("https://www.instagram.com/")
        # currentUrl == self.driver.current_url
        time.sleep(2)
        login_button = self.driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        currentUrl = driver.current_url
        
        print(redirectURL)
        print(currentUrl)
        if redirectURL == currentUrl:
            message = 'success'
        else:
            message = 'failed'
        return message
