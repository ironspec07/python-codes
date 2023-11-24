str = "hello"

for i in range(len(str)):
    if ord(str[i]) >= 97 and ord(str[i]) <= 122:
        s1 = chr(ord(str[i]) - 32)
        str = str[:i] + s1 + str[i+1:]
print(str)