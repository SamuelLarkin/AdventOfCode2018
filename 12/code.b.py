#!/usr/bin/env python

from __future__ import print_function

from utils import grow_generation
from utils import parse
from utils import grow


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        initial_state, rules = parse(f)

    print(initial_state)
    print(rules)
    width = 5000
    state = '.'*width + initial_state + '.'*width
    prev_count = 0
    for n in range(1100):
        state = grow(state, rules)

        count = 0
        for i, x in enumerate(state):
            if x == '#':
                count += i - width
        diff = count - prev_count
        prev_count = count
        print(n+1, count, diff)

    answer = (50000000000 - (n+1)) * diff + count
    print('Answer:', answer)
    # 250000045224 to high
    # 250000000219
