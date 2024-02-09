#!/bin/python3

import math
import os
import random
import re
import sys

'''
51Pa*0Lp*0e
aP1pL5e



'''

#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    # Write your code here
    senha = ""
    i = 0
    while i < len(s):
        print(s[i], senha)
        if not ((ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (
                ord(s[i]) >= 97 and ord(s[i])) <= 122):
            i = i + 1
        elif s[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            i = i + 1
        elif i + 1 < len(s) - 1 and ord(s[i]) >= 97 and ord(s[i + 1]) < 97:
            senha = senha + s[i + 1]
            senha = senha + s[i]
            senha = senha + '*'
            i = i + 3
        else:
            senha = senha + s[i]
            i = i + 1
    return (senha)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()