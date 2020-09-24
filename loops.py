"""
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task
Given an integer, n, print its first 10 multiples. Each multiple n X i (where ) (1<=i<=10)should be printed on a new line in the form: n x i = result.

Input Format:
            A single integer, n.
Output Format:
            Print  10 lines of output; each line  (where 1<= i<=10 ) contains the  of n X i in the form:
            n x i = result. """


import math
import os
import random
import re
import sys

"""def multiplication_num(x):
    for i in range(1, 11):
        result = x * i
        i+= 1
        print('{xx} * {ii} = {rr}'.format(xx=x, ii=i, rr=result))
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        result = n* i
        print('{x} x {ii} = {rr}'.format(x=n, ii=i, rr=result))
        i+= 1

""" OUTPUTS:
3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30"""