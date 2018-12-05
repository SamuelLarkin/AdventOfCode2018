#!/usr/bin/env python

from __future__ import print_function

from tqdm import tqdm
from polymer import read_polymer
from polymer import reduce_polymer

polymer = read_polymer()

alphabet = set(polymer)
print('alphabet:', len(alphabet), alphabet)
print(len(polymer))


smallest_polymner = polymer
for a in tqdm(set(map(lambda x: x.lower(), alphabet))):
    exclusion = set((a, a.upper()))
    filtered_polymer = filter(lambda x: x not in exclusion, polymer)
    smallest_polymner = min(smallest_polymner,
            reduce_polymer(filtered_polymer),
            key=lambda x: len(x))

answer = len(smallest_polymner)
print('Answer:', answer)
# 4996
