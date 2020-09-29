""" PROBLEM STATEMENTS: https://www.hackerrank.com/challenges/30-recursion/problem """
import math
import os
import random
import re
import sys
#count=0
# Complete the factorial function below.
def factorial(x):
    while (x>=1):
        if x == 1:
            return 1
        else:
            return x * factorial(x-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
