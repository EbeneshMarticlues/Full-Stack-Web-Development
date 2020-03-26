#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ebene
#
# Created:     19-02-2020
# Copyright:   (c) ebene 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def bank():
    pass
    while True:
        print("your welcome")
        print('''May i help you?
              if you want
              credit: press 0
              withdraw:press 1
              balance check: press 2
              exit : press 9
              ''')
        Amount_acc = int(10000)
        balance = Amount_acc
        var = input()
        var = int(var)
        if(var==1):
            amount=int(input("enter your amount"))
            Amount_acc+=amount
            balance=Amount_acc
            print("your new amount is:",balance)
        elif(var==2):
            amount=int(input("enter your amount"))
            Amount_acc=Amount_acc-amount
            balance=Amount_acc
            print("your new balance is:",balance)
        elif(var==3):
            balance=Amount_acc
            print("your balance is:",balance)
        elif(var==9):
            print("Exit")
            break
        else:
            print("Key invalid.Enter the correct key")


def password_check(User,Pass,un,ps):
    pass
    if(User==un):
        pass
        if(Pass==ps):
            print ("Login matched.your welcome")
        elif(Pass!=ps):
            for i in range (0,5):
                a=input("password:")
                a=hash(a)
                if(a==Pass):
                    print("welcome")
                    bank()
                    break
                else:
                    print("Password mismatched")
    else:
        while True:
            us = input("enter user name")
            us=hash(us)
            if(us==User):
                pass
                password_check(User,Pass,us,ps)



if __name__ == '__main__':
    main()
Username="ebi"
Password="ebi@123"
Username=hash(Username)
Password=hash(Password)
u=input("enter your username")
p=input("enter your password")
u=hash(u)
p=hash(p)

if((Username==u) and (Password==p)):
    pass
    bank()
else:
    password_check(Username, Password, u, p)

