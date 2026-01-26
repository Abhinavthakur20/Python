# mutable , allows duplicates , store multiple data types
a=[20,22,2,3,45,12]
# print(a[5])



#traversing the list
for i in range (len(a)):
    print(a[i])

# directly on value traverse

for i in a:
    print(i)




#List Methods

l=[12,269,3,84,4,46,4,5,6]
l.append(8)
l.append(10)


l.insert(6,7)

l.extend([12,13,14,15])
l.remove(10)
l.pop(3)
ind=l.index(14)
occurence = l.count(4)
print(occurence)
print(ind)
print(l)
l.sort()
l.reverse()

new_l= l.copy()
l.clear()







#to print +ve and -ve values diff in list

lists=[20,-21,11,25,-54,43,59,-98,-88,44]
print("postive numers:-")
for i in lists:
    if i>=0:
        print(i)
print("negative numbers:-")
for i in lists:
    if i<0:
        print(i)





# Mean or Average of the list elements

num=[12,32,43,54,3,43,43,222,42,51]
sum=0
for i in num:
    sum+=i
print(sum/len(num))





#find the laregest element of the list and index

lis1=[12,32,43,54,3,43,43,222,42,51]
greatest=lis1[0]
index=0

for i in range(len(lis1)):
    if lis1[i]>greatest:
        greatest=lis1[i]
        index =i
print(greatest,index)




# find the second largest number

lis2=[12,32,43,54,3,43,43,222,42,200]
large= lis2[0]
slarge=lis2[0]

for i in lis2:
    if i>large:
        slarge=large
        large=i
    elif i>slarge:
        slarge=i
print(slarge,large)




#check if list is sorted or not


list3=[12,13,23,3,45,67,78]


for i in range(len(list3)-1):
    if list3[i] < list3[i+1]:
        continue
        
    else:
        print("list is not sorted")
        break
else:
    print("sorted")





