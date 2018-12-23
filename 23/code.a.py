#!/usr/bin/env python3

from __future__ import print_function

from nanobot import parse
from nanobot import count_in_range




if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        nanobots = parse(f)

    print('Answer:', count_in_range(nanobots[0], nanobots))
    # 463
