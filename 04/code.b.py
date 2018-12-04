#!/usr/bin/env python

from __future__ import print_function

from reader import read_data
from functools import reduce
import numpy as np
from collections import defaultdict

with open('data.txt','r') as f:
    data = read_data(f.readlines())

print(data)

guard = max(data.values(), key=lambda g: g.schedule.max)
print(guard)
#Datum(
#   id=163,
#   schedule=Schedule(schedule=array([ 0,  1,  2,  3,  3,  4,  4,  3,  3,  4,  5,  5,  6,  6,  6,  6,  6, 8,  9,  9, 10, 10, 11, 11, 11, 12, 13, 14, 16, 18, 17, 15, 13, 11, 10, 10, 10, 12, 11,  9, 10,  9,  9,  9,  9, 10,  9,  6,  8,  8,  7, 5,  5,  2,  1,  1,  1,  1,  0,  0]),
#      max=18,
#      argmax=29),
#   log=[(3, 47), (17, 38), (5, 41), (12, 33), (1, 29), (45, 51), (2, 7), (10, 28), (22, 54), (27, 32), (49, 56), (26, 31), (37, 44), (48, 51), (28, 32), (25, 30), (40, 47), (18, 50), (9, 47), (28, 33), (37, 39), (48, 49), (29, 34), (43, 46), (52, 53), (56, 58), (17, 53), (28, 43), (24, 31), (29, 53), (20, 24), (29, 39), (44, 52)],
#   total_sleeping_time=447,
#   longest_nap=44)


answer = guard.id * guard.schedule.argmax
print('Answer:', answer)
# 4727
