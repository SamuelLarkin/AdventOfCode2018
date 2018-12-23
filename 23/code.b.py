#!/usr/bin/env python3

from __future__ import print_function

from nanobot import parse
from nanobot import count_in_range
from nanobot import Nanobot




if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        nanobots = parse(f)

    min_ = min(map(lambda n: n.x, nanobots))
    max_ = max(map(lambda n: n.x, nanobots))
    print(min_, max_)
    me = Nanobot(0,0,0,0)
    for n in nanobots:
        print(n.distance(me))
