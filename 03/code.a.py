#!/usr/bin/env python

from __future__ import print_function

from functools import reduce
from reader import read_data
import numpy as np


FABRIC_SIZE = 1000


def mask(x):
    m = np.zeros((FABRIC_SIZE,FABRIC_SIZE), dtype=np.int)
    m[x.bottom:x.top+1, x.left:x.right+1] = 1
    return m



with open('data.txt', 'r') as f:
    data = read_data(f)

if False:
    test = ('#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2')
    data = read_data(test)

#print(data)
bitmap = reduce(lambda accumulator, x: x + accumulator, map(mask, data), np.zeros((FABRIC_SIZE,FABRIC_SIZE), dtype=np.int))
answer = np.count_nonzero(bitmap > 1)

print('Answer:', answer)
# 107043
