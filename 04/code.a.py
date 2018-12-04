#!/usr/bin/env python

from __future__ import print_function

from reader import read_data
from functools import reduce
import numpy as np

with open('data.txt','r') as f:
    data = read_data(f.readlines())

print(data)


sleepiest_guard = max(data.values(), key=lambda g: g.total_sleeping_time)
print('sleepiest_guard:', sleepiest_guard)
#sleepiest_guard: Datum(
#   id=1601,
#   schedule=Schedule(schedule=array([ 1,  2,  3,  4,  4,  4,  6,  6,  6,  6,  6,  5,  5,  6,  7,  7,  6, 6,  6,  7,  9,  8,  7,  8,  9,  9, 10, 10,  9,  9,  9,  9,  9,  9, 11, 10, 10, 11, 11, 10, 11, 12, 12, 12, 12, 13, 14, 13, 12, 11, 11, 10, 10,  9,  9,  8,  8,  3,  3,  0]),
#      max=14,
#      argmax=46),
#   log=[(6, 16), (53, 59), (1, 11), (20, 57), (38, 48), (0, 35), (39, 54), (8, 21), (40, 53), (26, 59), (19, 39), (6, 8), (23, 49), (55, 57), (2, 22), (46, 57), (14, 40), (13, 39), (47, 55), (34, 47), (40, 47), (3, 28), (37, 53), (45, 55), (34, 38), (41, 51), (54, 57), (20, 57), (24, 59)],
#   total_sleeping_time=483,
#   longest_nap=37)

answer = sleepiest_guard.id * sleepiest_guard.schedule.argmax
print('Answer:', answer)
#73646
