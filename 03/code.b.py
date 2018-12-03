#!/usr/bin/env python

from __future__ import print_function

from reader import read_data
import numpy as np



def intersect(a, b):
    if a.right < b.left or b.right < a.left:
        return False
    if a.top < b.bottom or b.top < a.bottom:
        return False
    return True



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
