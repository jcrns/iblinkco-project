from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass
import time
VALUE = dict()
class twitterBot:

    def __init__(self, username, password, text):
        self.username = username
        self.password = password
        # mobileView.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        self.driver = webdriver.Chrome()
        self.text = text

    def getFollowerInfo(self):
        print("Attempting to get info")
        clickUserAccount = self.driver.find_element_by_xpath("//*[@id='page-container']/div[1]/div[1]/div/div[1]/span/a/span/b")
        clickUserAccount.click()
        time.sleep(1)
        # Getting User Information
        getUserTweets = self.driver.find_element_by_xpath("//*[@id='page-container']/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/a/span[3]").text
        print(getUserTweets)

        getUserFollowing = self.driver.find_element_by_xpath("//*[@id='page-container']/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[2]/a/span[3]").text
        print(getUserFollowing)

        getUserFollowers = self.driver.find_element_by_xpath("//*[@id='page-container']/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[3]/a/span[3]").text
        print(getUserFollowers)

        getUserBio = self.driver.find_element_by_xpath("//*[@id='page-container']/div[4]/div/div/div[1]/div/div/div/div[1]/p").text
        print(getUserBio)

        getUserLocation = self.driver.find_element_by_xpath("//*[@id='page-container']/div[4]/div/div/div[1]/div/div/div/div[1]/div[1]/span[2]/a").text
        print(getUserLocation)


        userInfo = [getUserTweets, getUserFollowing, getUserFollowers, getUserBio, getUserLocation]
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
        try:
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
                print(currentUrl)
        except Exception as e:
                print(e)
                VALUE['message'] = 'failed'
        return VALUE


    def postTweet(self):
        # Logging in to post tweet
        twitterBot.login(self)
        try:
            if self.text != '':
                # Putting information in to tweet
                tweetInput = self.driver.find_element_by_xpath("//*[@id='tweet-box-home-timeline']")
                tweetInput.click()
                tweetInput.send_keys(self.text)
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

    def changeBio(self):

        # Going to home page
        clickUserAccount = self.driver.find_element_by_xpath("//*[@id='page-container']/div[1]/div[1]/div/div[1]/span/a/span/b")
        clickUserAccount.click()

        time.sleep(1)

        # Going to Edit Profile
        clickEditProfile = self.driver.find_element_by_xpath("//*[@id='page-container']/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[8]/div/button/span")
        clickEditProfile.click()

        # Click Bio
        editBio = self.driver.find_element_by_xpath("//*[@id='user_description']")
        editBio.click()

        # Deleting Bio
        editBio.clear()

        time.sleep(1)

        # Entering New Bio
        editBio.send_keys(self.text)


        # Saving Changes
        clickSave = self.driver.find_element_by_xpath("//*[@id='page-container']/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[8]/div/div/button[2]")
        clickSave.click()

    def changeBioReturn(self):
        try:
            twitterBot.login(self)
            twitterBot.changeBio(self)
            VALUE['message'] = 'success'
        except Exception as e:
            print(e)
            VALUE['message'] = 'failed'

        return VALUE
