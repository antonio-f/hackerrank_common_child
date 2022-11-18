#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

from collections import defaultdict

def commonChild(s1, s2):
    # Write your code here
    prev = defaultdict((int))
    for i in range(len(s1)):
        cur = defaultdict(int)
        for j in range(len(s2)):
            cur[j] = prev[j - 1] + 1 if s1[i] == s2[j] else max(cur[j - 1], prev[j])
        prev = cur
    return prev[len(s2)-1]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
