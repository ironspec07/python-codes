# name = input("what's your name? ")
# print(f"hello,{name}")


# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))
    
# for name in sorted(names):
#     print(f"hello,{name}")


# writing and creating a file:-

#name = input("what's your name? ")

# file = open("names.txt","w")--> w(write) will re-create a file each time we run the code and erae the old content.
#to tackel the above problem we use a(append)
# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()


# with open("names.txt","a") as file: # 'with' keyword is used to get rid of close line as it automatically opens and closes the file. 
#     file.write(f"{name}\n")


# Reading a file:-

# with open("names.txt","r") as file:
#     # lines = file.readlines()
#     for line in file:
#         print("hello", line.rstrip())

# Sorted:-

# sorted(Iterable,/,*,key=None,reverse=false)

# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
        
# for name in sorted(names):
#     print(f"hello,{name}")
    
# for name in sorted(names,reverse=True):#reverse list
#     print(f"hello,{name}")
    
# CSV- commma seperated value

# with open ("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         name , house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
        
# Sorted in csv:-

# students = []
# with open ("students.csv") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         # students.append(f"{name} is in {house}")
# # for student in sorted(students):
# #     print(student)
#         student = {"Name":name , "House": house}
#         # student["Name"] = name
#         # student["House"] = house
        
#         students.append(student)
        
# for student in students:
#     print(f"{student['Name']} is in {student['House']}")
    
# Sorting dictionaries:

students = []
with open ("students.csv") as file:
    for line in file:
        name , house = line.rstrip().split(",")
        student = {"Name":name , "House": house}
        students.append(student)
        
        def get_name(student):
            return student["Name"]
        
for student in sorted(students , key = get_name , reverse=True):
    print(f"{student['Name']} is in {student['House']}")