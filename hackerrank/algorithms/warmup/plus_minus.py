#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives,negatives,zeroes = 0,0,0
    arr_length = len(arr)
    # Count the occurences of zeroes, positive and negative numbers in the array
    for i in arr:
        if i > 0:
            positives = positives + 1
        elif i < 0:
            negatives = negatives + 1
        else:
            zeroes = zeroes + 1
    # compute and print the ratio w.r.t the array length
    print("{:.6f}".format(positives/arr_length))
    print("{:.6f}".format(negatives/arr_length))
    print("{:.6f}".format(zeroes/arr_length))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
