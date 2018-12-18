#!/usr/bin/env python

from __future__ import print_function

from utils import convolve
from utils import reader
from collections import Counter
from collections import defaultdict
from tqdm import trange


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


def score(acres):
    return Counter(acres.ravel().tolist())['|']



def find_repetition(iterable):
    seen = defaultdict()
    values = []
    for i, value in iterable:
        if value in seen:
            return seen[value], values[seen[value]:]
        values.append(value)
        seen[value] = i



if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        acres = reader(f)

    def generator():
        for _ in range(10000):
            acres = convolve(acres)
            yield acres

    future = 1000000000
    start, serie = find_repetition(generator)

    #assert serie[617] == serie2[(617 - 584) % len(serie2)], '{} {}'.format(serie[617], serie2[(617 - 584) % len(serie2)])
    answer = serie[(future - start) % len(serie)]

    print('Answer:', answer)
    # 236300  too high
