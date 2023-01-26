#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
<<<<<<< HEAD
        print("{:c}".format(ord(str[i]) - num), end=)
    print()
=======
        print("{:c}".format(ord(str[i]) - num), end=' ')
    print("")
>>>>>>> 6760bfbca15a98c288ab72fc9c03c388abd92ee1
