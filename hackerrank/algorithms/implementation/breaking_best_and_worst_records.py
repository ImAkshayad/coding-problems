#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    records = [0, 0]
    min = scores[0]
    max = scores[0]
    for i in range(1,len(scores)):
        if scores[i] < min:
            records[1] = records[1] + 1
            min = scores[i]
        elif scores[i] > max:
            records[0] = records[0] + 1
            max = scores[i]
    return records
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
