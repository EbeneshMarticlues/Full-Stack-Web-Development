def ebi():
    bal=1000000
    print("hello Ebi Welcome To Marticlues Bank We Are Having "+str(bal)+"amount Balance")

    z=int(input("Enter Your Amount To withdraw : "))
    withd=bal-z


    print("Your Balance : "+str(withd))


username="ebi"
password="ebi@111"

user=input("Enter Your User Name : ")


if username==user:
    print("Enter Your Password")
else:
    print("user name is Wrong")

password1=input("Enter Your Password :")

if password==password1:
    print("Enter Your OTP")
else:
    print("Password Is Worng ")

import random

i=int(random.random()*10000)

print(i)
x=int(input("Enter Your OTP :"))

if(i==x):
    print(ebi())
else:
    print("Get Out Idiot")
