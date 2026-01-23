num1 = int(input("enter no1-"))
num2 = int(input("enter no2-"))

if num1+num2 > 100:
    print("memory full")
elif num1+num2<=60:
    print("memory under control")
else:
    print("success")


if num1>num2:
    print(f"{num1}is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else :
    print("both are equals")



gender = input("enter your gender as character (M or F)-")

if gender=="M" or gender == "m":
    print("hi good morning sir")
elif gender=="F" or gender=="m":
    print("hi good morning mam")
else :
    print("Unidentified")





if num1 %2==0:
    print("number is even")

else:
    print("number is odd")






name= input("enter your name -")
age = int(input("enter your age -"))

if age>=18:
    print(f"heloo {name} you are eligible for voting")
elif age<18:
    print(f"heloo sorry {name} you are not eligible")
else:
    print("enter valid age")





year = int(input("enter year -"))

if year%100==0 and year%400==0:
    print("its a leap year")
elif year%100!=0 and year%4==0:
    print("its a leap year")
else:
    print("its a normal year")








