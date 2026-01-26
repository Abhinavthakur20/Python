# SET = MUTABLE -- NO DUPLICATES -- UNORDERED _CAN NOT ACCESSED USING INDEX
# SEMI HATEROGENEOUS _ STORES --- STRING NUMBERS TUPLES BUT DONT EVERYTHING

set = {1,2,3,4,5,5,66,66}
print(set)

set1 = {1,2,3,4,5,5,66,66,88}
print(set1)

# set removes if duplicates exist
# set does not have index value
# each value in a set is hashed using hash function in python
a=hash("Hello")
print(a)


# Set methods

s={1,2,3,4,5,6}
s.add(12)
s.remove(3)
s.discard(6)
s.pop()
print(s)
#s.clear()



# UNION -- INTERSECTION -- DIFFERENCE -- SYMMETRIC DIFFERNECE

#(A|B) UNION
#(A&B) INTERSECTION
#(A-B) DIFFERENCE
#(A^B) SYMMETRIC DIFFERNECE

A= {1,2,3}
B= {3,4,5}

union = A.union(B)
print(union)



P = {1,2,2,3,4,5}
Q = {4,5,8,1,6,9}

common= P.intersection(Q)
print(common)





S = {3,4,5,8}
T = {2,6,3,4}

diff = S.difference(T)
print(diff)
# 8,5





C = {1,2,3,4,5}
D = {3,4,5}

symD = C.symmetric_difference(D)
print(symD)
#1,2








