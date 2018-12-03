#!/usr/bin/env python

from __future__ import print_function

import re
from collections import namedtuple
from itertools import combinations
from functools import reduce
import numpy as np



Data = namedtuple('Data', ('id', 'left', 'top', 'width', 'height'))




def read_data(iterable):
    # #1 @ 596,731: 11x27
    data_re = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    data = []
    for l in iterable:
        m = re.match(data_re, l.strip())
        assert m, 'Error with the regular expression'
        data.append(Data(*map(int, m.group(1,2,3,4,5))))

    return data


def mask(x):
    m = np.zeros((1000,1000), dtype=np.int)
    m[x.top:x.top+x.height, x.left:x.left+x.width] = 1
    return m



with open('data.txt', 'r') as f:
    data = read_data(f)

if False:
    test = ('#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2')
    data = read_data(test)

#print(data)
bitmap = reduce(lambda accumulator, x: x + accumulator, map(mask, data), np.zeros((1000,1000), dtype=np.int))
answer = np.count_nonzero(bitmap > 1)

print('Answer:', answer)
# 107043
