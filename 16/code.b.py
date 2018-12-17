#!/usr/bin/env python

from __future__ import print_function

from opcodes import opcodes
import json
from utils import parse_data
from utils import SetEncoder
import sys



def perfect_matching_by_peeling(possible_opcodes):
    op_codes_by_id = [None] * 16
    # Let's add op_id to opcodes
    while len(possible_opcodes) > 0:
        op_id, op_name = min(possible_opcodes.items(), key=lambda x: len(x[1]))

        assert len(op_name) == 1, op_name
        op_name = op_name.pop()
        #print(op_id, op_name)
        #op_codes_by_id[op_id] = opcodes[op_name]
        op_codes_by_id[op_id] = op_name

        del(possible_opcodes[op_id])
        for a, b in possible_opcodes.items():
            b -= {op_name}
        for op_id, names in list(filter(lambda x: len(x[1]) == 0, possible_opcodes.items())):
            del(possible_opcodes[op_id])
        #print('possible_opcodes:', len(possible_opcodes), json.dumps(possible_opcodes, indent=3, cls=SetEncoder))

    return op_codes_by_id



def bipartite_perfect_matching(edges):
    # This is a better method since the previous method hits a maximum recursion limit.
    import random

    ass = [-1] * len(edges) # their number -> my number
    for v in range(len(edges)):
        while v != -1:
            w = random.choice(edges[v])
            v, ass[w] = ass[w], v

    return ass






if __name__ == '__main__':
    possible_opcodes = parse_data()
    for i, names in sorted(possible_opcodes.items()):
        print(i, names)

    # [Matching (graph theory)](https://en.wikipedia.org/wiki/Matching_(graph_theory))
    # [](https://www.reddit.com/r/adventofcode/comments/a6p5ih/day_16_part_2_solving_opcodes/ebwsivn)
    if False:
        import random
        import sys
        op_id_to_name = list(opcodes.keys())
        print('op_id_to_name:', op_id_to_name)
        op_name_to_id = { op_name: i for i, op_name in enumerate(op_id_to_name) }
        print('op_name_to_id:', op_name_to_id)
        edges = [ { op_name_to_id[n] for n in names } for names in possible_opcodes.values() ]
        print('edges:', edges)
        ass = [-1] * len(opcodes) # their number -> my number
        def assign(v):
            w = random.choice(list(edges[v]))
            u, ass[w] = ass[w], v
            if u != -1: assign(u)
        for i in range(len(opcodes)):
            assign(i)
        print(ass)
        sys.exit(0)
        # [11, 6, 0, 8, 4, 7, 10, 12, 3, 2, 5, 1, 15, 13, 9, 14]

    if True:
        op_id_to_name = list(opcodes.keys())
        print('op_id_to_name:', op_id_to_name)

        op_name_to_id = { op_name: i for i, op_name in enumerate(op_id_to_name) }
        print('op_name_to_id:', op_name_to_id)

        # Edges are links between the unknown opcode_id and their possible opcode ids in opcodes.opcodes
        #edges = [ [ op_name_to_id[n] for n in possible_opcodes[i] ] for i in range(len(possible_opcodes.keys())) ]
        edges = [ [ op_name_to_id[n] for n in names ] for i, names in sorted(possible_opcodes.items()) ]
        assert len(edges) == 16
        for i,e in enumerate(edges):
            print(i, e)

        associated_opcodes = bipartite_perfect_matching(edges)
        for v, u in enumerate(associated_opcodes):
            assert u in edges[v], '{} not in {}'.format(u, edges[v])

        print(associated_opcodes)
        print(list(op_id_to_name[i] for i in associated_opcodes))
        # opcodes number read from the data.txt file is match to my opcodes which are in opcodes.opcodes
        # opcode 0 is match to my opcode 11
        # opcode 5 is match to my opcode 7
        # [11, 6, 0, 8, 4, 7, 10, 12, 3, 2, 5, 1, 15, 13, 9, 14]



    op_codes_by_id = perfect_matching_by_peeling(possible_opcodes)
    print(op_codes_by_id)

    import sys
    sys.exit(0)


    # Run the program.
    with open('data.b.txt', 'r') as f:
        registers = [0] * 4
        for l in f:
            instruction = list(map(int, l.strip().split()))
            op_codes_by_id[instruction[0]](instruction, registers)

    print('Answer:', registers[0])
    # 600
