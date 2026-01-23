# accept an int an print hello world n times

n = int(input("enetr the value"))
for i in range(n):
    print("hello world")



# reverse for loop


n = int(input("enter the value"))
for i in range(n,1,-1):
    print(i)



# print natural numbers

n= int (input("enter your numbers"))
for i in range(1,n+1):
    print(i)


# print table with input

n = int(input("enter value -"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")




# print sum of n 


n = int(input("enter value -"))
sum =0
for i in range(1,n+1):
    sum+=i
    
print(sum)





# factorial of number


n = int(input("enter value -"))
fact =1
for i in range(1,n+1):
    fact=fact*i
    
print(fact)



n = int(input("enter value -"))
even =0
odd = 0
for i in range(1,n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"even{even} odd {odd}")



# factors

n= int(input("which number factors do you want-:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)



# perfect number 


n= int(input("enter the number to check its perfect or not:-"))
sum =0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum == n:
    print("n is a perfect number")
else:
    print("n is not a perfect number")



# prime number

n = int(input("enter value to check prime or not -"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1

if count==2:
    print("num is prime")
else:
    print("num is not prime")






# string questions

# reverese string
a= "SHERIYANS"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)



# palindrome  string

a= "NAMAN"
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if a==b:
    print("its a palindrome")
else :
    print("not")


