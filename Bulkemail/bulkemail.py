from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import re
from getuserinput import get_userinputs
from validateemail import validateemail
from datetime import datetime

if __name__ == "__main__":
    print("Thanks for using Bulkemail sender.")

    #### Get Inputs    
    details = get_userinputs()

    
    if details == False:
        exit()
    
    #### Validate emails provided in csv
    emailstor = ""
    chkmail = validateemail()
    if chkmail == False:
        exit()
    else:
        print("[+] Email Validity confirmed")
        emailstor = pd.read_csv("Bulkemail\EmailAddress.csv")
    
    #### Sending the email
    
    log1 = open("text.txt","w+")
    log1.close()

    print("[+] Starting to send email....")

    for i in range(0,len(emailstor.index)):
        # Getting the content for the heading.        
        ttemp1 = emailstor.loc[i]["TO"].split(";")
        tempto =",".join(ttemp1)
        tempcc = str()
        if type(emailstor.loc[i]["CC"]) == str:
            ttemp2 = emailstor.loc[i]["CC"].split(";")
            tempcc = ",".join(ttemp2)
        else:
            tempcc = ""
        tempbcc = str()
        if type(emailstor.loc[i]["BCC"]) == str:
            ttemp3 = emailstor.loc[i]["BCC"].split(";")
            tempbcc = ",".join(ttemp3)
        else:
            tempbcc = ""

        # Create email object for storing email template
        emailobj = MIMEMultipart("alternative")
        emailobj["From"] = details[0]
        #Assigning what ever was taken to email object
        emailobj["To"] = tempto
        emailobj["Cc"] = tempcc
        emailobj["Bcc"] = tempbcc
        emailobj["Subject"] = details[4]
        print(f"\n\n\nTo :{tempto}\nCc :{tempcc}\nBcc :{tempbcc}\n")

        # Send email
        mael = str()
        with open("Bulkemail\Email.txt","r") as fil:
            mael = fil.read()
        emailobj.attach(MIMEText(mael,"html"))
        send_email = SMTP(details[2],587)
        send_email.starttls()
        send_email.login(emailobj["From"],details[1])
        send_email.send_message(emailobj)        
        with open("log.txt","a") as log:
            tmptext = str(datetime.now()) + ";" + tempto + ";" + tempcc + ";" + tempbcc +"\n"
            log.write(tmptext)
        send_email.close()

    
    print("Email has been sent.")    

