#!/usr/bin/env python


from __future__ import print_function

from utils import parse
from utils import intersection
from utils import corner
import numpy as np
from collections import Counter



test_data = '''
/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/
'''
test_data = test_data.split('\n')[1:-1]


def find_last_cart(track, carts):
    tick = 0
    cart_map = { c.p: c for c in carts }
    while len(carts) > 1:
        tick += 1
        for c in sorted(carts, key=lambda c: c.p):
            if not c._alive:
                continue

            del(cart_map[c.p])
            c.move_on_track(track)

            # Check for collision and remove carts who collided.
            if c.p in cart_map and cart_map[c.p]._alive:
                c._alive = False
                cart_map[c.p]._alive = False
                del(cart_map[c.p])
            else:
                cart_map[c.p] = c


        carts = list(filter(lambda x: x._alive, carts))
        #print(tick)
        #if debug:
        #    print('track:\n', '\n'.join(track), sep='')
        #print('carts:', '\n'.join(map(str,carts)), sep='')

    return carts[0]





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        track, carts = parse(f)

    debug = False
    if debug:
        track, carts = parse(test_data)
        assert len(carts) == 9

    assert len(carts) % 2 == 1
    carts = sorted(carts, key=lambda c: c.p)
    print('track:\n', '\n'.join(track), sep='')
    print('carts:', '\n'.join(map(str, carts)), sep='')

    cart = find_last_cart(track, carts)
    answer = cart.p

    print(carts)
    print('Answer:', answer)
    # [Nice visualization](https://mk-hill.github.io/TrialAndError/cart-visualizer/)
    # Answer:  129,62  WRONG
    # 59,137   WRONG 
    # 138,89  WRONG
    # 69,67



'''
< collided with > at 117,62 on tick 178
15 carts left.
v collided with ^ at 147,96 on tick 307
13 carts left.
^ collided with v at 64,107 on tick 364
11 carts left.
^ collided with > at 117,53 on tick 587
9 carts left.
v collided with ^ at 20,136 on tick 633
7 carts left.
< collided with < at 33,69 on tick 1384
5 carts left.
'''
