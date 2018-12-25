#!/usr/bin/env python

from __future__ import print_function

from reader import parse
from utils import find_constellations
from utils import manhattan_distance_all





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        stars = parse(f)

    distances = manhattan_distance_all(stars)
    constellations = find_constellations(distances)


    print('Answer:', len(constellations))
    # 375
