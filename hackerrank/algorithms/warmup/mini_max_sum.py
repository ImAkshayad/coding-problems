#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min, max = 0, 0
    for i in range(0,len(arr)):
        if i == 0:
            min = min + arr[i]
        elif i == len(arr)-1:
            max = max + arr[i]
        else:
            min = min + arr[i]
            max = max + arr[i]
    print("{0} {1}".format(min,max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
