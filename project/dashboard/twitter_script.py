from selenium import webdriver
from getpass import getpass
import time

VALUE = dict()
class twitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def getFollowerInfo(self):
        print("Attempting to get info")

        # Getting User Information
        getUserTweets = self.driver.find_element_by_xpath("//*[@id='page-container']/div[1]/div[1]/div/div[2]/ul/li[1]/a/span[2]").text
        print(getUserTweets)

        getUserFollowing = self.driver.find_element_by_xpath("//*[@id='page-container']/div[1]/div[1]/div/div[2]/ul/li[2]/a/span[2]").text
        print(getUserFollowing)

        getUserFollowers = self.driver.find_element_by_xpath("//*[@id='page-container']/div[1]/div[1]/div/div[2]/ul/li[3]/a/span[2]").text
        print(getUserFollowers)

        userInfo = [getUserTweets, getUserFollowing, getUserFollowers]
        VALUE['userData'] = userInfo

    def login(self):
        print('working')
        driver = self.driver

        redirectURL = 'https://twitter.com/'

        # Attempting to login
        driver.get("https://twitter.com/login")
        time.sleep(2)
        username_field = driver.find_element_by_class_name("js-username-field")
        password_field = driver.find_element_by_class_name("js-password-field")
        username_field.send_keys(self.username)
        time.sleep(1)
        password_field.send_keys(self.password)
        time.sleep(1)
        driver.find_element_by_class_name("EdgeButtom--medium").click()
        time.sleep(2)

        # Getting current url
        currentUrl = driver.current_url


        print(redirectURL)
        print(currentUrl)

        # Verify user had success logging in by comparing urls
        if redirectURL == currentUrl:

            twitterBot.getFollowerInfo(self)
            # Sending message success to views file
            VALUE['message'] = 'success'
            self.driver.close()
        else:
            self.driver.close()

            # Sending message failed to views file
            VALUE['message'] = 'failed'
        return VALUE
