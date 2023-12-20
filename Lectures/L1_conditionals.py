# > greater than 
# < less than 
# >= greater than equal to
# <= less than equal to
# == comparision
# != not equal to
##########################IF-ELIF-ELSE#################################################################################################
x = int(input("what's number 1: "))
y = int(input("what's number 2: "))

if x<y:
    print("num 1 is less than num 2")
elif x>y:
    print("num 1 is greater than num 2")
else:
    print("num 1 is equal to num 2")

##########################OR-NOT EQUALTO#################################################################################################
if x<y or x>y:
    print("num1 not equals to num2")
if x != y:
    print("num1 not equals to num2")

########################## AND #################################################################################################
score = int(input("score: "))

if score>=90 and score<=100:
    print("Grade S")
elif score>=80 and score<=90:
    print("Grade A")
elif score>=70 and score<=80:
    print("Grade B")
elif score>=60 and score<=70:
    print("Grade C")
elif score>=50 and score<=60:
    print("Grade D")
elif score>=40 and score<=50:
    print("Grade E")
else:
    print("Grade F")

########################## + - * / % #################################################################################################
x = int(input("what's number: "))
if x%2==0:
    print("even")
else:
    print("odd")

def main():
    x = int(input("what's number: "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    # if(n%2==0):
    #     return True
    # else:
    #     return False
    # return True if n%2==0 else False
    return (n%2==0)
main()

########################## MATCH (SWITCH IN JAVA)#################################################################################################
name = input("What's your name? ").capitalize()

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")