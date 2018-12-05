#!/usr/bin/env python

from __future__ import print_function

from polymer import read_polymer
from polymer import reduce_polymer

polymer = read_polymer()

alphabet = set(polymer)
print('alphabet:', len(alphabet), alphabet)
print(len(polymer))

reduced_polymer = reduce_polymer(polymer)
answer = len(reduced_polymer)
print('Answer:', answer)
# 9348
