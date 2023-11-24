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

