#!/usr/bin/env python3

from __future__ import print_function

from collections import Counter

with open('data.txt', 'r') as f:
    data = [ Counter(l.strip()) for l in f ]

#print(data)
twos = 0
threes = 0
for d in data:
    print(d.most_common())
    # find the counts of counts
    coc = Counter(c for l, c in d.most_common())
    print(coc)
    if 2 in coc:
        twos += 1
    if 3 in coc:
        threes += 1

print('Answer:', twos * threes)
