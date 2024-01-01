# # str="I am ironman"
# # str.endswith("man")
# # str.startswith("i")
# # user_input= input()
# # print(user_input)


# # response = input()
# # shouted_response = response.upper()
# # print(shouted_response) 

# ########TYPECASTING#############
# # num = input() #taking input

# # num = int(num) #typecasting string to int

# # num = str(num) #typecasting int to str

# # num = num+num
# # print(num)

# # num = num*7
# # print(num)

# ########CONVERSION & SPLITING#############

# top10Comp = "google,microsoft,apple,facbook,netflix,amazon"
# company = top10Comp.split(",")
# print(company)

# for c in company:
#     print(c)
    


# # isalpha() -> alphabetic
# # isalnum() -> alphanumeric
# # isdigut() -> digit

# from math import pi
# radius = eval(input("What's Radius? "))
# if radius>0:
#     area = (radius**2)*pi
#     cir = 2*pi*radius
#     print(f"area of circle is: {area:.2f} and it's circumference is: {cir:.2f}")


# sales = int(input("What's sales? "))
# basic = 4000
# conve = 500
# da = 1.10*basic
# if sales<100000:
#     hra = 0.1*basic
#     incentive = 0.04*sales
#     bonus = 500
# else:
#     hra = 0.2*basic
#     incentive = 0.1*sales
#     bonus = 1000

# # print(f"basic: {basic}\n HRA: {hra}\n DA: {da}\n Conveyance: {conve}\n Incentive: {incentive}\n Bonus: {bonus}\n ")
# # print("Total Salary: ",(sales+basic+bonus+hra+da+incentive+conve))

# from tabulate import tabulate
# mydata = [
#     ["Sales ", sales], 
#     ["Basic", basic], 
#     ["HRA",hra],
#     ["DA",da],
#     ["conveyance",conve],
#     ["Incentive",incentive],
#     ["Bonus",bonus],
#     ["Gross Salary",(sales+basic+bonus+hra+da+incentive+conve)] 
# ]
# head = ["Particulars", "Amount(in RS)"]
# print(tabulate(mydata, headers=head, tablefmt="grid"))

# age = int(input("What's age? "))
# if age>18:
#     print("Adult")
# elif age>=13 and age<18:
#     print("Teenager")
# elif age>=0 and age<13:
#     print("Child")
# else:
#     print("not a valid age")

# # wap to input 3 nos and check if 1st is lessthan or grater than other two
# a = int(input("What's num-1? "))
# b = int(input("What's num-2? "))
# c = int(input("What's num-3? "))

# if a>b:
#     if a>c:
#         print("Num-1 is greatest")
#         if b>c:
#             print("Num-2 is second greatest and Num-3 is smallest")
#         else:
#             print("Num-3 is second greatest and Num-2 is smallest")
#     else:
#         print("Num-3 is greatest")
#         print("Num-1 is second greatest and Num-2 is smallest")
        
# elif b>a:
#     if b>c:
#         print("Num-2 is greatest")
#         if a>c:
#             print("Num-1 is second greatest and Num-3 is smallest")
#         else:
#             print("Num-3 is second greatest and Num-1 is smallest")
#     else:
#         print("Num-3 is greatest")
#         print("Num-2 is second greatest and Num-1 is smallest")

# sub1 = eval(input("Enter marks of subject-1: "))
# sub2 = eval(input("Enter marks of subject-2: "))
# sub3 = eval(input("Enter marks of subject-3: "))
# sub4 = eval(input("Enter marks of subject-4: "))
# sub5 = eval(input("Enter marks of subject-5: "))

# per = (sub1+sub2+sub3+sub4+sub5)/5
# print(f"percentage: {per}%")

# if per>=90:
#     print("Distinction")
# elif per>=80:
#     print("First Class")
# elif per>=70:
#     print("Second Class")
# elif per>=60:
#     print("Pass")
# else:
#     print("Fail")

# total = 0
# for x in range(10,20,2): #from 10 to 20 in interval of 2
#     total = total + x
#     print(x)
# print(f"the total is: {total}")    

# print("the capital letter A to Z are as follows: ")
# for i in range(65,91,1):
#     print(chr(i),end=" ")
# print()
# for i in range(97,123,1):
#     print(chr(i),end=" ")
# print()



#print("patterns")
# num = 65
# for i in range(1,4,1):
#     num=num+1
#     for j in range(65,num,1):
#         print(chr(j),end=" ")
#     print()
# for i in range(1,3,1):
#     num=num-1
#     for j in range(65,num,1):
#         print(chr(j),end=" ")
#     print()

# def printMax(num1,num2):
#     if num1>num2:
#         print("num-1 is greater")
#     elif num2>num1:
#         print("num-2 is greater")
#     else:
#         print("num-1 and num-2 are equal")

# def main():
#     a = int(input("enter num-1: "))
#     b = int(input("enter num-2: "))
#     printMax(a,b)

# main()


# def calc_fact(a):
#     fact = 1
#     for i in range(1,a+1):
#         fact = fact*i
#     print(f"factorial is: {fact}")

# def main():
#     a = int(input("enter number: "))
#     calc_fact(a)

# main()

# def solve(a,b,c,d,e,f):
#     x = (d+e-b+f)/(a+d-b+c)
#     y=(a+f-c+a)/(a+d-b+c)
#     return (x,y)
# def main():
#     xsol , ysol = solve(2,3,4,1,2,5)
#     print (f"x solution is {xsol}\ny solution is {ysol}")
# main()

# def fancy_print(text , color="black" , background="white" , style="normal" , justify="left" ):
#     fancy_print("hi" , style="bold")
#     fancy_print("hi" , color="yello" , background="black")
#     fancy_print("hi")

# import math
# def calc_distance (x1,y1,x2,y2):
#     dx = x2-x1
#     dx = math.pow(dx,2)
#     dy = y2-y1
#     dy = math.pow(dy,2)
#     z = math.pow((dx+dy),2)
    
#     return z
# print(f"Distance = {calc_distance(4,4,2,2):.2f}")

# def quad_Eqn(a,b,c):
#     d = (b*b)-(4*a*c)
#     if d>0 :
#         print("The eqn has two real roots")
#     elif d<0 :
#         print("The eqn has two complex root")
#     else:
#         print("The eqn has one real root")

# def main():
#     a = int(input("What's a: "))
#     b = int(input("What's b: "))
#     c = int(input("What's c: "))
#     quad_Eqn(a,b,c)
# main()

# list1 = [10,20,30,40,50,60]

# for i in range(6):
#     print(list1[i])

# def getNum():
#     while True:    
#         try:
#             num = int(input("What's the number? "))
#             return num
#         except ValueError:
#             print("not a valid number")
# def main():
#     x = getNum()
#     print(f"provided number is: {x}")

# main()

# list1 = [1,2,3,4,5]
# print(list1[:2])
# print(list1[::-1])

# def takeList():
#     n = int(input("What's the size of list? "))
#     lst = []
#     print("enter elements of list")
#     for i in range(0,n):
#         a = int(input())
#         lst.append(a)
#     return lst
# def calcAvg(lst):
#     print("sum = " , sum(lst))
#     print("Avg = " , (sum(lst)/len(lst)))
    

# def main():
#     calcAvg(takeList())

# main()

# def taketuple(n):
#     tup = ()
#     print("Enter elements of tuple:")
#     for _ in range(n):
#         elem = input()
#         tup += (elem,)
#     return tup
# def calcAvg(tup, n):
#     total_sum = 0
#     for x in tup:
#         total_sum += int(x)
#     avg = total_sum / n
#     print(f"Sum = {total_sum}\nAverage = {avg}")
    

# def main():
#     n = int(input("What's the size of tuple? "))
#     calcAvg(taketuple(n),n)

# main()

# from itertools import count


# D = {}
# D["Laptop"] = "MAC"
# D["count"] = 10
# print(D)
# print("I want %(count)d %(Laptop)s Laptops"%D)

# class MethodOverload:
#     def add(self , a , b, c=None):
#         if c is not None:
#             print(a+b+c)
#         else:
#             print(a+b)

# py = MethodOverload()

# py.add(1,2)
# py.add(1,2,3)

# class MyClass:
#     def my_method(self , arg1 , arg2 = None , arg3 = None):
#         if arg3 is not None:
#             print(f"Recieved Three arguments: {arg1} {arg2} {arg3}")
#         elif arg2 is not None:
#             print(f"Recieved Two arguments: {arg1} {arg2}")
#         else:
#             print(f"Recieved argument: {arg1}")
# py = MyClass()
# py.my_method("hello")
# py.my_method("hello","world")
# py.my_method("hello","dark","world")
            

# from re import X


# class OperatorOverload:
#     def __init__(self,x):
#         self.X = X
#     def __add__(self,other):
#         print(f"Value of obj_1 is: {self.X}")
#         print(f"Value of obj_2 is: {other.X}")
#         return OperatorOverload(self.X + other.X)
    
# obj1 = OperatorOverload(20)
# obj2 = OperatorOverload(40)
# obj99 = OperatorOverload(100)

# obj3 = obj1+obj2+obj99

# print("final result:",obj3.X)

# class Point:
#     def set_cordinates(self , X ,Y):
#         self.X = X
#         self.Y = Y
# class New_Point(Point):
#     def draw(self):
#         print('Locate point x = ',self.X ,'on X axis')
#         print('Locate point y = ',self.Y ,'on Y axis')
        
#         p = New_Point()
#         p.set_cordinates(10,20)
#         p.draw()
        
# class A:
#     name = ' '
#     age = 0
# class B(A):
#     height = ' '
# class C(B):
#     weight = ' '

#     def Read(self):
#         print("please enter the folowing values")
#         self.name = input("What's name? ")
#         self.age = int(input("What's Age? "))
#         self.height= input("What's height? ")
#         self.weight= input("What's weight? ")
#     def Display(self):
#         print(f"details are:/nName = {self.name}/nAge = {self.age}/nHeight = {self.height}/nWeigth = {self.weight}"
#         )
# OB1.C()
# Ob1.Read()
# Ob1.Display()

# class A:
#     a = 0
# class B:
#     b = 0
# class C(A,B):
#     c = 0

#     def Read(self):
#         self.a = int(input("What's a? "))
#         self.b = int(input("What's b? "))
#         self.c = int(input("What's c? "))
#     def Display(self):
#         print('a = ',self.a)
#         print('b = ',self.b)
#         print('c = ',self.c)
# Ob1 = C()
# Ob1.Read()
# Ob1.Display()

# open file in read mode 
# myfile = open("demofile.txt"


# myFile = open("demofile.txt",'w')

# # retrive and print the mode of all file
# print("File Mode:", myFile.mode)

# # retrive and print the name of the file
# print("File Name: , myfile.name")
# # close the file
# myFile.close()

# file_path = "employees.txt"
# with open(file_path , 'r') as file:
#     for line in file:
#         name,department,salary = line.strip().split(",")
#         print(f"Employee:{name}, Department:{department} , Salary:{salary}")

# import os

# with os.scandir('test/') as entries:
#     for entry in entries:
#         print(entry.name)
    

# myobject = open("myFile.txt",'w')
# lines = ["hello everyone\n","Writing multiline strings\n","this is the third line"]
# myobject.writelines(lines)
# myobject.close()
# myobject = open("myFile.txt",'r')
# print(myobject.read())
# # myobject.close()
# try:
#     with open("nonexistant_file.txt",'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError as e:
#     print(f"File not found {e}")
# except IOError as e:
#     print(f"an IOerror occured: {e}")
# else:
#     print("file read successfully")
# finally:
#     print("cleanup or additional actions can be performed here")
############################################## DIRECTORIES #####################################
# import os 
# directory_path = "test1"
# # files = os.listdir(directory_path)
# # scan = os.scandir(directory_path)
# if os.path.exists(directory_path):
#     print("dir exists")
# else:
#     print("dir does not exists")

# import os
# import shutil
# dir_to_remove = "test2"
# os.rmdir(dir_to_remove)
