#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here

def avg(num_list):
    new_list = list()
    number = 0

    while number < len(num_list):
        va = num_list[number]
        number = number + 1
        new_list.append(int(va))

    average = sum(new_list) / len(new_list)
    return float(average)


if __name__ == '__main__':

    nums = list(map(int, input().split()))
    print(type(nums))
    res = avg(nums)

    print('%.2f' % res + '\n')
