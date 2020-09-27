"""https://www.hackerrank.com/challenges/30-arrays/problem"""

import math
import os
import random
import re
import sys

#if __name__ == '__main__':
n =input()
arr = list(map(int, input().rstrip().split()))
result_list = []
for i in range(int(n)):
    result_list.append(arr[n - i - 1])
print(" ".join(map(str, result_list[:])))

"""sample inputs :
            4
            1 4 3 2
OUTPUTS:
            2 3 4 1
"""