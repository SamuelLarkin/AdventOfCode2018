#!/usr/bin/env python

from __future__ import print_function

from utils import read_map
from game import Game




if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        m, p, w = read_map(f)
        game = Game(m, w, p)
        step, score = game.combat(5000)
        print(score)
        # 208413 too low
        # 210843 too low
