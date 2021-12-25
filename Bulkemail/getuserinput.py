from getpass import getpass
from checkconn import check_conn
import re

def get_userinputs():
    flg = int()
    flg = 0
    username = str()
    counter = 0
    while flg==0 and counter <=3:
        username = input("Please enter the from email address : ")
        if re.match('(([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2})))|([a-z0-9A-z])*\.([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2}))',username):
            flg = 1
        elif counter <=2:
            print("!!!Incorrect format. Please try again!!!")
            counter+=1
        else:
            print("!!!Incorrect format. Incorrect password has been entered 3 times please check the email address and try again")
            return False
    #Resetting the flag and counter to use somewhere else
    flg = 0
    counter = 0
    password = str()
    email_link = str()
    port = int()
    while flg == 0 and counter <= 3:
        password = getpass(prompt="Please enter the password for the email : ")
        email_link = input("Please enter the SMTP URL : ")
        port = input("Please enter the port : ")
        if check_conn(username,password,email_link,port) == True:
            flg = 1
            print("Details validated")
        elif counter<=2:
            print("Unable to validate the connection. Please re-enter the details")
            counter += 1
        else:
            print("Unable to validate the connection. There were more than 3 tries.\nPlease check the details and try again")
            return False
    email_subject = input("Please enter the email subject: ")
    return username,password,email_link,port,email_subject

if __name__ == "__main__" :
    test = get_userinputs()
    print(test[0])
    print(type(test))
