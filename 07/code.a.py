#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ./code.a.py > Makefile ; \make | paste -sd '' -
# https://en.wikipedia.org/wiki/Tsort
# cut -d ' ' -f 2,8 < data.txt | tsort | paste -sd '' -
#SCPLAMYVQWUNHODTRGKBJEFXZI  # NOT GOOD
#SCLPWMNVHOQATGYDKUBRJEFXZI  # NOT GOOD


from __future__ import print_function


from collections import defaultdict
from utils import parse_dependencies
from utils import test_data
from utils import topological_sort_generator





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        deps = parse_dependencies(f)
        alphabet = set(map(chr, range(ord('A'), ord('Z')+1)))

    debug = False
    if debug:
        deps = parse_dependencies(test_data)
        alphabet = set(map(chr, range(ord('A'), ord('F')+1)))

    forward_deps  = defaultdict(lambda: set())
    backward_deps = defaultdict(lambda: set())
    for p, c in deps:
        forward_deps[p].add(c)
        backward_deps[c].add(p)
    print(backward_deps)

    answer = ''.join( topological_sort_generator(backward_deps) )
    print ('Answer:', answer)
    # SCLPAMQVUWNHODRTGYKBJEFXZI
