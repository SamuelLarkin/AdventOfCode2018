#!/usr/bin/env python

from __future__ import print_function

import re
from collections import namedtuple
from itertools import combinations
from functools import reduce
import numpy as np



DataBase = namedtuple('Data', ('id', 'left', 'top', 'width', 'height'))
class Data(DataBase):
    @property
    def bottom(self):
        return self.top + self.height - 1
    @property
    def right(self):
        return self.left + self.width - 1


def intersect(a, b):
    if a.right < b.left or b.right < a.left:
        return False
    if a.bottom < b.top or b.bottom < a.top:
        return False
    return True



def read_data(iterable):
    # #1 @ 596,731: 11x27
    data_re = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    data = []
    for l in iterable:
        m = re.match(data_re, l.strip())
        assert m, 'Error with the regular expression'
        data.append(Data(*map(int, m.group(1,2,3,4,5))))

    return data


with open('data.txt', 'r') as f:
    data = read_data(f)

if False:
    test = ('#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2')
    data = read_data(test)

#print(data)
for i, a in enumerate(data):
    if all(map(lambda x: not intersect(a,x), data[:i] + data[i+1:])):
        answer = a.id


print('Answer:', answer)
# 346
