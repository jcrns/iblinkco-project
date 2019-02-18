from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


REALUSER = False
class InstagramBot:
    # declaring variable parameters
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()


    def closeBrowser(self):
        self.driver.close()

    def login(self):
        # declaring variable for function
        message = ''
        redirectURL = 'https://www.instagram.com/'

        # Attempting to log user into instagram
        print("Logging In")
        driver = self.driver
        driver.get("https://www.instagram.com/")
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

        # Getting to current url
        currentUrl = driver.current_url

        # Finding Profile button and clicking it

        # # Getting user information
        # userNumberOfPost = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span")
        # userFollowers = len(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a"))
        # userFollowing = len(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a"))

        # print(userNumberOfPost)

        print(redirectURL)
        print(currentUrl)

        # Verify user had success logging in by comparing urls
        if redirectURL == currentUrl:
            profileButton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
            profileButton.click()
            time.sleep(2)
            message = 'success'
        else:
            self.driver.close()
            message = 'failed'
        return message
