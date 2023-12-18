
# ########################## WHILE #################################################################
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# ########################## FOR ####################################################################
# for i in [0,1,2]:
#     print("meow")


# for i in range(3):
#     print("meow")

# for _ in range(3):#if the variable i is of no use we can use _ instead of i 
#     print("meow")

# print("meow\n"*3 , end="")#another way to print meow three times

# ########################## GETTING A +VE INPUT ######################################################
# while True:
#     n = int(input("what's the number? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# def main():
#     num = get_number()
#     meow(num)

# def get_number():
#     while True:
#         n = int(input("what's the number? "))
#         if n > 0:
#             return n

# def meow(nu):
#     for i in range(nu):
#         print("meow")

# main()

# ########################## LISTS #########################################################################

# students = ["Hermione","Harry","Ron"]

# # print(students[0])
# # print(students[1])
# # print(students[2])

# for student in students:# printing values in list
#     print(student)

# print(len(students))# prints length of list

########################## DICT #############################################################################

# students = {
#     "Hermione":"Griffindor",
#     "Harry":"Griffindor",
#     "Ron":"Griffindor",
#     "Draco":"Slytherin"
# }
# #print(students["Ron"])

# for student in students:
#     #print(students)#to print just students name 
#     print(student , students[student],sep=", ")#to print both key and value 

########################## LIST OF DICT #######################################################################
students = [
    {
        "name":"Hermione",
        "house":"Griffindor",
        "patronus":"Otter"
    },
        {
        "name":"Harry",
        "house":"Griffindor",
        "patronus":"Stag"
    },
        {
        "name":"Ron",
        "house":"Griffindor",
        "patronus":"Jack Russell Terrier"
    },
        {
        "name":"Draco",
        "house":"Slytherin",
        "patronus":None
    }
]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=" | ")

########################## NESTED LOOPS ########################################################################
def main():
    print_column(3)
    print_square(3)
    
def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()    
        
main()