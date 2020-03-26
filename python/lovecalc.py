import random

a=int(random.random()*101)

b=input("Enter Your Name : ")

c=input("Enter Your Lovers Name : ")

if(a<=50):
    print("Your Love : "+str(a)+"%")
    print("Low")
elif(a>=50&a<=99):
    print("Your Love : "+str(a)+"%")
    print("nutral")
elif(a==100):
    print("Your Love : "+str(a)+"%")
    print("Strong")



