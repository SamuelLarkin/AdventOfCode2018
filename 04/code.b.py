#!/usr/bin/env python

from __future__ import print_function

from reader import read_data
from functools import reduce
import numpy as np
from collections import defaultdict

with open('data.txt','r') as f:
    data = read_data(f.readlines())

print(data)

sleep_parttern = defaultdict(lambda: np.zeros((60,), dtype=np.int))
data2 = {}
for guard_id, log_time in data.items():
    for s, w in log_time:
        mask = np.zeros((60,), dtype=np.int)
        mask[s:w] = 1
        sleep_parttern[guard_id] += mask
    data2[guard_id] = {
            'max': np.max(sleep_parttern[guard_id]),
            'argmax': np.argmax(sleep_parttern[guard_id]),
            }
    print(sleep_parttern[guard_id])
    print(data2[guard_id])

#print(sleep_parttern)
#print(data2)
answer = max(data2.items(), key=lambda a: a[1]['max'])
print(answer)

answer = answer[0] * answer[1]['argmax']
print('Answer:', answer)
