#!/usr/bin/env python

from __future__ import print_function

from utils import parse
from utils import combat





if __name__ == '__main__':
    first, top = 52, 100
    while first <= top:
        boost = (first + top) // 2
        with open('data.txt', 'r') as f:
            immune, infection = parse(f, boost)

        while len(immune) and len(infection):
            combat(immune, infection)

        score = immune.score()
        print(boost, score)
        if score > 0:
            top = boost
        else:
            first = boost


    print('Answer:', boost)
    # 4 wrong
    # 3 loops forever
    # 53
