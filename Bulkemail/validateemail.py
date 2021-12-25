from numpy import float64
import pandas as pd
import re

def validateemail():
    flg = 0
    csvfil = pd.read_csv("Bulkemail\EmailAddress.csv")
    print("\n[+]Checking email validity!!!")
    for i in range(0,len(csvfil.index)):
        if type(csvfil.loc[i]["TO"]) == str:
            tempto = csvfil.loc[i]["TO"].split(";")
            for j in tempto:
                if type(j) != float64 and not re.match('(([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2})))|([a-z0-9A-z])*\.([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2}))',j):
                    print(f"\nIncorrect value {j} in 'TO' email in row {i+2}. Kindly recheck the csv file.")
                    flg = 1
        if type(csvfil.loc[i]["CC"]) == str:
            tempcc = csvfil.loc[i]["CC"].split(";")
            for k in tempcc:
                if type(k) != float64 and not re.match('(([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2})))|([a-z0-9A-z])*\.([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2}))',k):
                    print(f"\nIncorrect value {k} in 'CC' email in row {i+2}. Kindly recheck the csv file.")
                    flg = 1
        if type(csvfil.loc[i]["BCC"]) == str:
            tempbcc = csvfil.loc[i]["BCC"].split(";")
            for l in tempbcc:
                if type(l) != float64 and not re.match('(([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2})))|([a-z0-9A-z])*\.([a-z0-9A-z])*@([a-zA-z])*\.((\w{3})|(\w{2}))',l):
                    print(f"\nIncorrect value {l} in 'BCC' email in row {i+2}. Kindly recheck the csv file.")
                    flg = 1
    if flg == 0:
        return True
    else:
        return False


            
        



    