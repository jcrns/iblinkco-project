# importing firebase
import pyrebase

class Authentication:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def fetchUser(self):
        # Used to connect to firebase server
        config = {
            'apiKey': "AIzaSyB-zW5qNKkTlfLzhbigIZkMWypJ4XMAAvY",
            'authDomain': "cpanel-8d88a.firebaseapp.com",
            'databaseURL': "https://cpanel-8d88a.firebaseio.com",
            'projectId': "cpanel-8d88a",
            'storageBucket': "cpanel-8d88a.appspot.com",
            'messagingSenderId': "955905061850"
          }
        firebase = pyrebase.initialize_app(config)

        auth = firebase.auth()
        user = authe.sign_in_with_email_and_password(self.email, self.password)

        db = firebase.database()
        return user
