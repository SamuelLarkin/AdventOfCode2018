#!/usr/bin/env python

from __future__ import print_function

from reader import read_data
from functools import reduce
import numpy as np

with open('data.txt','r') as f:
    data = read_data(f.readlines())

print(data)

data2 = {}
for guard, log_time in data.items():
    print(guard)
    print(log_time)
    total_sleeping_time = sum(map(lambda t: t[1]-t[0], log_time))
    longest_nap = max(map(lambda t: t[1]-t[0], log_time))
    print(guard, total_sleeping_time, longest_nap)
    data2[guard] = (total_sleeping_time, longest_nap)

print('data2:', data2)
print('data2.items{}:', data2.items())
print('data2.sorted:', sorted(data2.items(), key=lambda g: g[1][0]))

sleepiest_guard = max(data2.items(), key=lambda g: g[1][0])
print('sleepiest_guard:', sleepiest_guard)
#(1601, (483, 37))
guard_id, (total_sleeping_time, longest_nap) = sleepiest_guard
print(data[guard_id])

sleep_parttern = np.zeros((60,), dtype=np.int)
for s, w in data[guard_id]:
    mask = np.zeros_like(sleep_parttern)
    mask[s:w] = 1
    sleep_parttern += mask
print(sleep_parttern)
sleepiest_minute = np.argmax(sleep_parttern)

answer = guard_id * sleepiest_minute
print('Answer:', answer)
