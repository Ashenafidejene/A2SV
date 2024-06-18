#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here

    def sDigit(n):
        sum = 0 
        for i in range(len(n)):
            sum += int(n[i])
        if sum < 10 :
            return sum 
        else:
            return sDigit(str(sum))
    totalsum = 0 ; 
    for i in range (len(n)):
        totalsum+=int(n[i])
    totalsum*=k
    return sDigit(str(totalsum))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
