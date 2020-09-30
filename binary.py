""" problem statements: https://www.hackerrank.com/challenges/30-binary-numbers/problem """
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = format(n,'b')
    max_cons = 0;
    cons = 0;
    for number in binary:
        cons = cons + 1 if int(number) else 0
        max_cons = cons if max_cons < cons else max_cons
print(max_cons)