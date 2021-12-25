''' Mass email sending using python
Objective:
A user will save email in a text or html format
He will have list of users saved in csv format
The email will be sent to each user by python

Options available to user: Website of his choice
'''
from smtplib import SMTP
from getpass import getpass
import re

#Class to emulate key fields of email
class Email():
    to_email = str()
    subject = str()
    from_email = str()
    cc_email = str()
    bcc_email = str()
    body = str()
    def send_email(self):
        # This function is to send the email
        pass
#function to check connection
def check_conn(username,password,emaillink,port):
    try:
        email = SMTP(emaillink,port)
        email.starttls()
        email.login(username,password)
        email.close()
        return True
    except:
        return False
#fuction to get the email addresses from user



if __name__ == "__main__":
    print("This is only a class file!!!")

