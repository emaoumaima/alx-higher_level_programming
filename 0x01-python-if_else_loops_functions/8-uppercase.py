#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        if ord(str[j]) >= 97 and ord(str[j]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[j]) - num), end='')
    print()
