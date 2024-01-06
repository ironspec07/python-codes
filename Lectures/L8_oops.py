# # Represents a student with multiple variables

# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")


# # Modularizes getting student's name and house

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")


# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()

# # Returns student as tuple, unpacking it


# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house 


# if __name__ == "__main__":
#     main()

# # Returns student as tuple, without unpacking it


# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)


# if __name__ == "__main__":
#     main()

# # Demonstrates immutability of tuples, removes parentheses

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house


# if __name__ == "__main__":
#     main()

## Stores student as (mutable) list


def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()