#!/usr/bin/env python

from __future__ import print_function

from utils import parse_data





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        clays = parse_data(f)

    print(clays)
