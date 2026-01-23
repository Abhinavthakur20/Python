# to access each digit

a= int(input("enter number :-"))
while a>0:
    print(a%10)
    a= a//10




#reverse the numbers

a= int(input("enter number :-"))
rev=0
while a>0:
    rev = rev*10+a%10
    a= a//10
print(rev)





# check palindrome

a= int(input("enter number :-"))
copy =a
rev=0
while a>0:
    rev = rev*10+a%10
    a= a//10
if rev==copy:
    print("this is palindrome number")
else:
    print("this is not")




