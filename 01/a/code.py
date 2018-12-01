#!/usr/bin/env python

from __future__ import print_function

with open('../data.txt', 'r') as f:
    data = f.readlines()
data = map(lambda x : float(x.strip()), data)
print(sum(data))
