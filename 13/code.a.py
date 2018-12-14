#!/usr/bin/env python


from __future__ import print_function

from utils import parse
from utils import intersection
from utils import corner
import numpy as np
from collections import Counter



test_data = '''
/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   
'''
test_data = test_data.split('\n')[1:-1]


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        track, carts = parse(f)

    debug = False
    if debug:
        track, carts = parse(test_data)

    carts = sorted(carts, key=lambda c: c.p)
    print('track:\n', '\n'.join(track), sep='')
    print('carts:', carts)

    for tick in range(2000):
        carts = sorted(carts, key=lambda c: c.p)
        for c in carts:
            c.position += c.direction
            t = track[c.position[0]][c.position[1]] 
            if t in '/\\':
                c.direction = corner[t](c.direction)
            elif t == '+':
                c.direction = intersection[c.next_move](c.direction)
                c.next_move = (c.next_move + 1) % 3
            elif t == ' ':
                assert False
        print(tick)
        if debug:
            print('track:\n', '\n'.join(track), sep='')
            print('carts:', carts)
        collision = Counter(c.p for c in carts)
        answer = collision.most_common(1)[0]
        if answer[1] > 1:
            answer = answer[0]
            break


    print('Answer:', answer)
    # [Nice visualization](https://mk-hill.github.io/TrialAndError/cart-visualizer/)
    # Answer: 117,62
