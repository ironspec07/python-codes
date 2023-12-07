s1 = input("Enter a string: ")
res = "  " in s1
print("Double spaces present? "+ str(res))
s1 = s1.replace("  "," ")
print(s1)