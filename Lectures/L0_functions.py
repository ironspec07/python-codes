# taking name as input
name = input("what's your name? ") 
#removing whitespaces from string
name = name.strip()
#capitalizing first character of string
name = name.capitalize()
#capitalizing the first letter of each word
name = name.title()
#chaining functions
name = name.strip().title()
#spliting username into firstname and lastname and storing into two variables
first,last = name.split(" ") 
# printing
print("hello," + name) 
print("hello,",name) # second way of printing with two argument

# print(*objects, sep=' ', end='\n', file=None, flush=False)

# 1-*objects --> this implies that the print function can take as many strings as we want

# 2-sep=' ' --> this gives space between multiple argument

# 3-end='\n' --> this takes the cursor to new line 

print("hello,",end="") # another way of printing in same line
print(name)

print("hello,",name,sep="") # another way of printing with two argument without space

print(f"hello,{name}")# printing using format string

print(f"hello,{first}")# printing firstname 
print(f"hello,{last}")# printing lastname 

#######TYPECASTING###################################################################################
num = input("enter number ") #taking input

num = int(num) #typecasting string to int

num = str(num) #typecasting int to str

num = num+num
print(num)

num = num*7
print(num)

# round function to convert from float to int
# round(number [,ndigits])

# number --> value to be converted (takes only one value)
# ndigits --> number of places to be rounded to [optional]

x = float(input("enter number 1: "))
y = float(input("enter number 2: "))

z = round(x+y)
w = x/y

print(f"{z:,}")#prints sum in currency style --> 1,000(us convention)
print(f"{w:.2f}")#prints two digits after decimal


#######DEFINING FUNCTION###########################################################################

def hello():
    print("hello,",end="")

name = input("what's your name? ")
hello()
print(name)

def hello2(to): #parameterizing hello
    print("hello,", to)

hello2(name)

def hello2(to="world"):#inialising hello with default value if user does not provide parameter
    print("hello,", to)

hello2()
#######################################################################################################
def main():#defining main function 
    name = input("what's your name? ")
    hello2(name)

def hello2(to): 
    print("hello,", to)

main() #calling main function

#scope of main is only in main function
####################################RETURNING########################################################
def main():#defining main function 
    num = int(input("what's num? "))
    print("square of number is " , square(num))

def square(n): 
    #return n*n #returning value
    #return n**2 #raising to the power of two
    return pow(n,2)#raising to the power of two
main() #calling main function