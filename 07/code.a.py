#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ./code.a.py > Makefile ; \make | paste -sd '' -
# https://en.wikipedia.org/wiki/Tsort
# cut -d ' ' -f 2,8 < data.txt | tsort | paste -sd '' -
#SCPLAMYVQWUNHODTRGKBJEFXZI  # NOT GOOD
#SCLPWMNVHOQATGYDKUBRJEFXZI  # NOT GOOD


from __future__ import print_function


from collections import defaultdict


def kahn(deps):
    """
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edge
    while S is non-empty do
	remove a node n from S
	add n to tail of L
	for each node m with an edge e from n to m do
	    remove edge e from the graph
	    if m has no other incoming edges then
		insert m into S
    if graph has edges then
	return error   (graph has at least one cycle)
    else 
	return L   (a topologically sorted order)
    """
    L = []
    start_symbol = alphabet - set(b for a,b in deps)
    assert len(start_symbol) == 1
    start_symbol = start_symbol.pop()
    print('start_symbol:', start_symbol)

    forward_deps  = defaultdict(lambda: set())
    backward_deps = defaultdict(lambda: set())
    for p, c in deps:
        forward_deps[p].add(c)
        backward_deps[c].add(p)
    print(backward_deps)

    S = [start_symbol]
    while len(S) > 0:
        n = S.pop(0)
        L.append(n)


try:
    from functools import reduce
except:
    pass

# https://rosettacode.org/wiki/Category:Python
def toposort2(data):
    # Ignore self dependencies
    for k, v in data.items():
        v.discard(k)
    # Add node with no dependencies
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update({item:set() for item in extra_items_in_deps})
    data = dict(data)

    while True:
        #print('a', data)
        ordered = set(item for item,dep in data.items() if not dep)
        if not ordered:
            break
        ordered = sorted(ordered)[0]
        yield ordered
        ordered = set(ordered)
        data = {
                item: (dep - ordered) for item,dep in data.items()
                if item not in ordered
                }
    assert not data, "A cyclic dependency exists amongst %r" % data
 


def parse_dependencies(f):
    deps = []
    for l in f:
        p = l.strip().split()
        deps.append((p[1], p[7]))
    return deps


test_data = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
        ]


def using_matrix_power():
    import numpy as np
    grid = np.zeros((6,6), dtype=np.int)
    for d, p in deps:
        d = ord(d) - ord('A')
        p = ord(p) - ord('A')
        grid[d,p] = 1

    print(grid)
    accumulator = np.ones_like(grid)
    for _ in range(2):
        accumulator = np.matmul(accumulator, grid)
        print(accumulator)

    from numpy.linalg import matrix_power
    print(matrix_power(grid, 2))


def using_make():
    print('all: I')
    for d, t in deps:
        print('{t}: {d}'.format(t=t, d=d))

    for l in alphabet:
        print('{}: ; @echo "$@"'.format(l))


class Position:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def __lt__(self, other):
        if self.position == other.position:
            return self.letter > other.letter
        else:
            return self.position < other.position

    def __str__(self):
        return 'l: {} p: {}'.format(self.letter, self.position)

    def __repr__(self):
        #return 'l: {} p: {}'.format(self.letter, self.position)
        return '({p} {l})'.format(l=self.letter, p=self.position)


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

    positions = { l: -1 for l in alphabet }
    print(positions)

    for k,v in forward_deps.items():
        print(k,sorted(v))

    start_symbol = alphabet - set(b for a,b in deps)
    assert len(start_symbol) == 1
    start_symbol = start_symbol.pop()
    print('start_symbol:', start_symbol)

    end_symbol = alphabet - set(a for a,b in deps)
    assert len(end_symbol) == 1
    end_symbol = end_symbol.pop()
    print('end_symbol:', end_symbol)

    def calculate_depth(s, deps, positions):
       for a in deps[s]:
           positions[a] = max(positions[a], positions[s]+1)
           calculate_depth(a, deps, positions)

    positions[end_symbol] = 0
    calculate_depth(end_symbol, backward_deps, positions)
    print(positions)

    a = sorted((Position(l, p) for l, p in positions.items()), reverse=True)
    print(a)
    answer = ''.join(b.letter for b in a)
    print('Answer:', answer)

    if False:
        positions = { l: 26 - d for l, d in positions.items() }
        print(positions)
        ordered = sorted(positions.items(), key= lambda a: (a[1], a[0]))
        print(ordered)

    answer = ''.join( toposort2(backward_deps) ))
    print ('Answer:', answer)
    # SCLPAMQVUWNHODRTGYKBJEFXZI
