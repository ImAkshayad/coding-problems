#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    converted_str = ''
    if s[-2:] == 'AM':
        if int(s[0:2]) == 12:
            converted_str = '00' + s[2:-2]
        else:
            converted_str = s[0:-2]
    else:
        if int(s[0:2]) == 12:
            converted_str = s[0:-2]
        else:
            converted_str = str(int(s[0:2]) + 12) + s[2:-2]
    return converted_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
