try:
    num = int(input("What's the number? "))
except ValueError:
    print("not a valid number")

print(num)