# #LIST INTRODUCTION
# marks = [3,5,6,"tony",True , 7 ,18 ,45 , 24 ,23 , 22,19,26]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-3])#negative index
# print(marks[len(marks)-3])#positive index
# print(marks[5-3])#negative index

# if 7 in marks:
#     print("yes")
# else:
#     print("No")

# if "Ad" in "Aditya":
#     print("yes")

# print(marks[1:4]) #[5,6,"tony"]

# print(marks[1:8]) #[5, 6, 'tony', True, 7, 18, 45]
# print(marks[1:8:2]) #[5, 'tony', 7, 45]

# lst = [i for i in range(4)]
# lst1 = [i*i for i in range(4)]
# print(lst)#[0, 1, 2, 3]
# print(lst1)#[0, 1, 4, 9]

# lst2 = [i*i for i in range(10) if i%2==0]
# print(lst2)#[0, 4, 16, 36, 64]

# #LIST METHODS

# l = [1,2,3,4,5,6]
# print(l)
# l.append(7) # adds element to the last of list
# print(l)

# l.sort()#sorts list in assending order
# l.sort(reverse=True) # sorts list in decending order
# print(l)

# l.reverse()#reverses the original list

# print(l.index(2))# returns the index of first occurence of given element

# print(l.count(2))# counts the number of times the given element is present in list

# m = l.copy() #copies elements of l into m without effecting the original list

# l.insert(1,3)#inserts the provided element into the provided index

# k = [7 , 45 , 18]
# l.extend(k) # means to push elemnts of k to the last of l
# print(l)

# #TUPLE 

# Tuples are immutable
# tuple of one element is considered as int if comma is missing

a = (1)
print(type(a)) # <class 'int'>

b = (1,)
print(type(b))# <class 'tuple'>

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1) # (1, 2, 2, 3, 5, 4, 6)
print(tuple2) # ('Red', 'Green', 'Blue')

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details) #('Abhijeet', 18, 'FYBScIT', 9.8)

