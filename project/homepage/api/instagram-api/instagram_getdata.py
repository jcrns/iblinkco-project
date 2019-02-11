from InstagramAPI import InstagramAPI
import instagram_credentials

api = InstagramAPI(instagram_credentials.INSTAGRAM_USERNAME, instagram_credentials.INSTAGRAM_PASSWORD)
api.login()
api.getProfileData()

#Show keys
api.LastJson.keys()

# Special function to get followers
def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

class display():

    # Creating Functions to display on webpage
    def getUserId(self):
        #creating variable
        user_id = api.LastJson['user']['pk']
        return user_id
    def getUserUsername(self):
        #creating variable
        user_username = api.LastJson['user']['username']
        return len(user_username)
    def getUserBiography(self):
        #creating variable
        user_biography = api.LastJson['user']['biography']
        return user_biography
    def getUserGender(self):
        #creating variable
        user_gender = api.LastJson['user']['gender']
        return user_gender
    def getUserBirthday(self):
        #creating variable
        user_birthday = api.LastJson['user']['birthday']
        return user_birthday
    def getUserIsPrivate(self):
        #creating variable
        user_userisprivate = api.LastJson['user']['is_private']
        return user_userisprivate
    def getUserEmail(self):
        #creating variable
        user_useremail = api.LastJson['user']['email']
        return user_useremail

    def getUserFollowers(self):

        # user_id = '1461295173'
        user_id = api.username_id

        # List of all followers
        followers = getTotalFollowers(api, user_id)
        # print(len(followers))
        return len(followers)
