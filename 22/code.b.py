#!/usr/bin/env  python

from __future__ import print_function

from cave import create_cave
from cave import rescue_target
from cave import rescue_target2





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        depth = int(f.readline().strip().split()[1])
        target = f.readline().strip().split()[1].split(',')
        target = tuple(map(int, target))
        print(depth, target)

    cave = create_cave(depth, target, 100)
    answer = rescue_target(cave, target)

    print('Answer:', answer)
    # 1025
