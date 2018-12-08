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
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        return sum(visit(node.children[i-1]) for i in node.metadata if i <= len(node.children))





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        tree = parse(f.readline())

    debug = False
    if debug:
        tree = parse(test_data)

    print(tree)

    answer = visit(tree)
    print('Answer:', answer)
    # 66
    # 25910
