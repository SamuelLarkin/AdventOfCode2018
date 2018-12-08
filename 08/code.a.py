#!/usr/bin/env python

from __future__ import print_function
from utils import parse
from utils import chain
from utils import test_data

try:
    from functools import reduce
except:
    pass



def visit(node):
    return sum(node.metadata) + sum(visit(n) for n in node.children)





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        tree = parse(f.readline())

    debug = False
    if debug:
        tree = parse(test_data)

    print(tree)

    answer = visit(tree)
    print('Answer:', answer)
    # 138
    # 40908
