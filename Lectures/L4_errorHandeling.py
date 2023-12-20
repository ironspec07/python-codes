try:
    num = int(input("What's the number? "))
except ValueError:
    print("not a valid number")
else:
    print(num)


def getNum():
    while True:
        try:
            num = int(input("What's the number? "))
            return num
        except ValueError:
            print("not a valid number")


def main():
    x = getNum()
    print(f"provided number is: {x}")
