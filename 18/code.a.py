#!/usr/bin/env python

from __future__ import print_function

from utils import convolve
from utils import reader
from utils import score





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        acres = reader(f)

    for _ in range(10):
        acres = convolve(acres)

    print('Answer:', score(acres))
    # 589931
