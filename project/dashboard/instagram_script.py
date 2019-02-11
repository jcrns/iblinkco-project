from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        print("Logging In")
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)

        redirectURL = 'https://www.instagram.com/#reactivated'
        currentUrl = driver.currentUrl


        for url in redirectURL:
            print("Checking if logged in")
            if url == currentUrl:
                print("Correct")
                REALUSER = True
                break
            else:
                print("Incorrect")
                REALUSER = false
