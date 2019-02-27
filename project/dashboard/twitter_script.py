from selenium import webdriver
from getpass import getpass
import time
VALUE = dict()
class twitterBot:

    def __init__(self, username, password, tweet):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.tweet = tweet

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

    def returnLogin(self):
        twitterBot.login(self)
        # Getting current url
        driver = self.driver
        currentUrl = driver.current_url
        redirectURL = 'https://twitter.com/'

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
    def postTweet(self):
        # Logging in to post tweet
        twitterBot.login(self)
        try:
            if self.tweet != '':
                # Putting information in to tweet
                tweetInput = self.driver.find_element_by_xpath("//*[@id='tweet-box-home-timeline']")
                tweetInput.click()
                tweetInput.send_keys(self.tweet)
                tweetButton = self.driver.find_element_by_xpath("//*[@id='timeline']/div[2]/div/form/div[3]/div[2]/button/span[1]")
                tweetButton.click()
                VALUE['message'] = 'success'
                self.driver.close()
            else:
                VALUE['message'] = 'failed'
                self.driver.close()

        except Exception as e:
            print(e)
            self.driver.close()

            VALUE['message'] = 'failed'

        return VALUE
