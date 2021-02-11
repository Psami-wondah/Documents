


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    x = n - 1
    arr = list(map(int, input().rstrip().split()))

    while x >= 0:
        print(arr[x], end='')
        x = x - 1
        print(' ', end='')