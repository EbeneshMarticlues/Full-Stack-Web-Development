import random

a=int(random.random()*10000)


print(a)

b=int(input("Enter Your OTP : "))

if a==b:
    print("Your OTP Is Right")
else:
    print("Your OTP Is Wrong Idot")
