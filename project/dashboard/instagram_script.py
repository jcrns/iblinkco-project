from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import sys


VALUE = dict()
class InstagramBot:
    # declaring variable parameters
    def __init__(self, username, password, text, number):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.text = text
        self.number = number

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


        getUserBio = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span").text

        userInfo = [getUserPost, getUserFollowers, getUserFollowing, getUserBio]
        VALUE['userData'] = userInfo

    def login(self):
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

    def returnLogin(self):
        InstagramBot.login(self)
        driver = self.driver
        # declaring variable for function
        message = ''
        redirectURL = 'https://www.instagram.com/'
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
                print(e)
                # Clicking notification button
                notificationButton = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[1]")
                notificationButton.click()
                try:
                    print(e)
                    InstagramBot.gotoProfile(self)
                    InstagramBot.getFollowerInfo(self)
                except Exception as e:
                    print(e)

            time.sleep(2)

            InstagramBot.closeBrowser(self)
            # Sending message success to views file
            VALUE['message'] = 'success'
        else:
            InstagramBot.closeBrowser(self)

            # Sending message failed to views file
            VALUE['message'] = 'failed'
        return VALUE

    def changeBio(self):

        # Getting to Profile Page
        self.driver.get("https://www.instagram.com/" + self.username)


        # Clicking edit profile
        editButton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/a/button")
        editButton.click()

        # Getting Textarea to change element
        time.sleep(1)
        editBio = self.driver.find_element_by_xpath("//textarea[@id='pepBio']")
        editBio.click()

        # Deleting Bio
        editBio.clear()
        time.sleep(1)

        # Entering New Bio
        editBio.send_keys(self.text)

        # Save Changes
        saveChangesButton = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/form/div[10]/div/div/button[1]")
        saveChangesButton.click()

        # Closing Browser
        self.driver.close()

    def changeBioReturn(self):
        try:
            InstagramBot.login(self)
            InstagramBot.changeBio(self)
            VALUE['message'] = 'success'
        except Exception as e:
            print(e)
            # Clicking notification button
            notificationButton = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]")
            notificationButton.click()
            time.sleep(3)
            try:
                print(e)
                InstagramBot.changeBio(self)
                VALUE['message'] = 'success'
            except Exception as e:
                    print(e)

        return VALUE

    def likePhoto(self, hashtag, maxNumber):

        # Logging In
        InstagramBot.login(self)
        driver = self.driver

        # Going To Url of Hashtag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(1)

        # Getting Photos
        pic_hrefs = []
        likes = 0
        print(maxNumber)
        for i in range(1, 7):
            try:
                # Scrolling Down the Page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                # Getting Post Element
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]

                # Adding Pictures to list of Photos and Verifying already seen picture will not be clicked on
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))

            except Exception as e:
                print(e)
            print(likes)

        # For loop to like photo
        for pic_href in pic_hrefs:
            if likes <= maxNumber:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(2, 4))

                # Attempting to like
                try:
                    like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
                    like_button.click()

                    time.sleep(range(0, random.randint(18, 28)))
                except Exception as e:
                    print(e)
                likes = likes + 1
                print(likes)
            else:
                print("Opperation Completed")
                VALUE['message'] = 'success'
                try:
                    self.driver.close()
                except Exception as e:
                    print(e)
                break

    def likePhotoReturn(self):
        tags = self.text
        numberOfLikes = int(self.number)
        tag = random.choice(tags)
        InstagramBot.likePhoto(self, tag, numberOfLikes)
        VALUE['message'] = 'success'
        return VALUE

    def followUser(self, hashtag, maxNumber):

        # Logging In
        InstagramBot.login(self)
        driver = self.driver

        # Going To Url of Hashtag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(1)

        # Getting Photos
        pic_hrefs = []
        follows = 0
        print(maxNumber)
        for i in range(1, 7):
            try:
                # Scrolling Down the Page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                # Getting Post Element
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]

                # Adding Pictures to list of Photos and Verifying already seen picture will not be clicked on
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))

            except Exception as e:
                print(e)
            print(follows)

        # For loop to like photo
        for pic_href in pic_hrefs:
            if follows <= maxNumber:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(2, 4))

                # Attempting to like
                try:
                    follow_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button')
                    follow_button.click()
                    time.sleep(2)
                except Exception as e:
                    print(e)
                follows = follows + 1
                print(follows)
            else:
                print("Opperation Completed")
                VALUE['message'] = 'success'
                try:
                    self.driver.close()
                except Exception as e:
                    print(e)
                break

    def followUserReturn(self):
        tags = self.text
        numberOfFollows = int(self.number)
        tag = random.choice(tags)
        InstagramBot.followUser(self, tag, numberOfFollows)
        VALUE['message'] = 'success'
        return VALUE
