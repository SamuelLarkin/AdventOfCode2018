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


def finc_collision_location(track, carts):
    cart_map = { c.p: c for c in carts }
    for tick in range(2000):
        carts = sorted(carts, key=lambda c: c.p)
        print('carts:\n', '\n'.join(map(str, carts)), sep='')
        for c in carts:
            del(cart_map[c.p])
            c.position += c.direction
            t = track[c.position[0]][c.position[1]] 
            if t in '/\\':
                c.direction = corner[t](c.direction)
            elif t == '+':
                c.direction = intersection[c.next_move](c.direction)
                c.next_move = (c.next_move + 1) % 3
            elif t == ' ':
                assert False
            assert t in '+-|><v^/\\', t

            # Check for collision and remove carts who collided.
            if c.p in cart_map and cart_map[c.p]._alive:
                c._alive = False
                cart_map[c.p]._alive = False
                return c.p
            else:
                cart_map[c.p] = c





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        track, carts = parse(f)

    debug = False
    if debug:
        track, carts = parse(test_data)

    carts = sorted(carts, key=lambda c: c.p)
    print('track:\n', '\n'.join(track), sep='')
    print('carts:', carts)

    answer = finc_collision_location(track, carts)


    print('Answer:', answer)
    # [Nice visualization](https://mk-hill.github.io/TrialAndError/cart-visualizer/)
    # Answer: 117,62
