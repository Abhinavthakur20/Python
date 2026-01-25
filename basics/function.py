def heloo():
    print("hi bro how are you")
heloo()





def sum(a,b):
    print(f"sum of the numbers is - {a+b}")

sum(45,45)
sum(25,25)
sum(50,125)


def name(name):
    print(f"my name is :- {name}")
name("Abhinav")




def intro(name,age):
    print(f"hi, my name is {name} and i'm {age} years old")

intro(name="abhi" ,age=12)



def greet(name="guest"):
    print(f"hello , {name}")
greet()
greet("bob")



#default

def add(a,b=45):
    print(f"sum of the numbers is - {a+b}")

add(45)






def palindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev = rev+st[i]

    if rev==st:
        print("palindrome")
    else:
        print("not a palindrome")

palindrome("naman")
palindrome("hello")
palindrome("Kunal")









def hi():
    return "hello world"
print(hi())




