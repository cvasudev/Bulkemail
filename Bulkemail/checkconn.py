from smtplib import SMTP

def check_conn(username,password,emaillink,port):
    try:
        email = SMTP(emaillink,port)
        email.starttls()
        email.login(username,password)
        email.close()
        return True
    except:
        return False
    
    

if __name__ == "__main__":
    print("This is a function page. Please do not run this as main!!!!")

