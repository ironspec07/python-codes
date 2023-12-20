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

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello,{name}")
    
for name in sorted(names,reverse=True):#reverse list
    print(f"hello,{name}")
    
# CSV- commma seperated value
