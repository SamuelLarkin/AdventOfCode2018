#!/usr/bin/env python

from __future__ import print_function

from itertools import cycle

with open('../data.txt', 'r') as f:
    data = map(lambda x: int(x.strip()), f.readlines())

seen = set()

frequency = 0
seen.add(frequency)
for i, x in enumerate(cycle(data)):
    frequency += x
    if frequency in seen:
        print(i, frequency)
        #print(seen)
        break
    seen.add(frequency)
