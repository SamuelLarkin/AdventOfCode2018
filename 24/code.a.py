#!/usr/bin/env python

from __future__ import print_function

from utils import parse
from utils import combat





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        immune, infection = parse(f)

    while len(immune) and len(infection):
        combat(immune, infection)

    print(immune.score())
    print(infection.score())
    # 15165
