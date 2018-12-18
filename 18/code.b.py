#!/usr/bin/env python

from __future__ import print_function

import utils
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
    for i, value in enumerate(iter(iterable)):
        print(i, value)
        if value in seen:
            return seen[value], values[seen[value]:]
        values.append(value)
        seen[value] = i



def generator(acres):
    for _ in range(10000):
        acres = convolve(acres)
        yield score(acres)





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        acres = reader(f)

    previous_score = 0
    for i, s in enumerate(generator(acres)):
        print(i, s, s-previous_score)
        previous_score = s

    future = 1000000000
    start, serie = find_repetition(generator(acres))
    print(start, serie)

    #assert serie[617] == serie2[(617 - 584) % len(serie2)], '{} {}'.format(serie[617], serie2[(617 - 584) % len(serie2)])
    answer = serie[(future - start) % len(serie)]

    print('Answer:', answer)
    # 236300  too high


'''
839 695 -24
840 673 -22
841 650 -23
842 632 -18
843 592 -40
844 556 -36
845 512 -44
846 502 -10
847 491 -11
848 485 -6
849 477 -8
850 496 19
851 509 13
852 530 21
853 549 19
854 576 27
855 599 23
856 625 26
857 644 19
858 669 25
859 682 13
860 695 13
861 703 8
862 710 7
863 709 -1
864 711 2
865 711 0
866 719 8
'''
