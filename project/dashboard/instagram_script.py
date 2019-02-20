from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


VALUE = dict()
class InstagramBot:
    # declaring variable parameters
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()


    def closeBrowser(self):
        self.driver.close()

    def gotoProfile(self):
        # Finding Profile button and clicking it
        profileButton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
        profileButton.click()
        print("clicking button")
        time.sleep(2)

    def getFollowerInfo(self):
        print("Attempting to get info")

        # Getting User info
        getUserPost = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span[1]").text
        print(getUserPost)

        getUserFollowers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
        print(getUserFollowers)

        getUserFollowing = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        print(getUserFollowing)

        userInfo = [getUserPost, getUserFollowers, getUserFollowing]
        VALUE['userData'] = userInfo

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

        # Getting current url
        currentUrl = driver.current_url

        print(redirectURL)
        print(currentUrl)
        # Verify user had success logging in by comparing urls
        if redirectURL == currentUrl:

            try:
                print("Executing First Try")
                InstagramBot.gotoProfile(self)
                InstagramBot.getFollowerInfo(self)
            except Exception as e:
                print("error")
                # Clicking notification button
                notificationButton = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]")
                notificationButton.click()
                try:
                    print("First Try Failed")
                    InstagramBot.gotoProfile(self)
                    InstagramBot.getFollowerInfo(self)
                except Exception as e:
                    print("error")

            time.sleep(2)

            InstagramBot.closeBrowser(self)
            # Sending message success to views file
            VALUE['message'] = 'success'
        else:
            InstagramBot.closeBrowser(self)

            # Sending message failed to views file
            VALUE['message'] = 'failed'
        return VALUE
