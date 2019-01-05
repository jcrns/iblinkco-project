# importing email library
import smtplib

# importing local file with info
import config

# importing user data to send email to user
from django.contrib.auth.models import User

emails = User.objects.filter(is_active=True).exclude(email='').values_list('email',flat=True)

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        #first argument is the person who sends the email while the second argument is the person the email is sent to
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, emails, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Thanks"
msg = "Thank you for being one of the few to sign up on iBlinkco before the initial launching of the website"

send_email(subject, msg)
