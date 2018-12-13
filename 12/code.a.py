#!/usr/bin/env python

from __future__ import print_function

from utils import grow_generation
from utils import parse


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        initial_state, rules = parse(f)

    print(initial_state)
    print(rules)
    width = 100
    state = grow_generation('.'*width + initial_state + '.'*width, rules, 20)
    print(state)

    count = 0
    for i, x in enumerate(state):
        if x == '#':
            count += i - width
    print(count)
