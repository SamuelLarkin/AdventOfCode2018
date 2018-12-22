#!/usr/bin/env python

from __future__ import print_function

from cave import create_cave
from cave import risk_level



if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        depth = int(f.readline().strip().split()[1])
        target = f.readline().strip().split()[1].split(',')
        target = tuple(map(int, target))
        print(depth, target)

    cave = create_cave(depth, target)
    answer = risk_level(cave)

    print('Answer:', answer)
    # 7402
