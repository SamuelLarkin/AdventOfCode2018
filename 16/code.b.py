#!/usr/bin/env python

from __future__ import print_function

from bipartite import bipartite_perfect_matching
from opcodes import op_id_to_name
from opcodes import op_name_to_id
from opcodes import opcodes
from utils import SetEncoder
from utils import parse_data
from copy import deepcopy
import json
import sys



def perfect_matching_by_peeling(possible_opcodes_):
    # This is a desctructive process, let's make a copy.
    possible_opcodes = deepcopy(possible_opcodes_)
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
        for op_id, names in filter(lambda x: len(x[1]) == 0, possible_opcodes.items()):
            del(possible_opcodes[op_id])
        #print('possible_opcodes:', len(possible_opcodes), json.dumps(possible_opcodes, indent=3, cls=SetEncoder))

    return op_codes_by_id



def match_opcodes(possible_opcodes, opcodes):
    assert len(possible_opcodes) == 16
    assert len(opcodes) == 16

    # Edges are links between the unknown opcode_id and their possible opcode ids in opcodes.opcodes
    try:
        # possible_opcodes is a hash
        # [4, 0, 15, 6, 8, 7, 2, 12, 10, 5, 11, 3, 9, 14, 13, 1]
        edges = [ [ op_name_to_id[n] for n in possible_opcodes[i] ] for i in range(len(possible_opcodes.keys())) ]
        edges = [ [ op_name_to_id[n] for n in names ] for i, names in sorted(possible_opcodes.items()) ]
        # [11, 6, 0, 8, 4, 7, 10, 12, 3, 2, 5, 1, 15, 13, 9, 14]
        #edges = [ [ op_name_to_id[n] for n in names ] for names in possible_opcodes.values() ]
    except:
        # possible_opcodes is an array
        # [4, 0, 15, 6, 8, 7, 2, 12, 10, 5, 11, 3, 9, 14, 13, 1]
        edges = [ [ op_name_to_id[n] for n in names ] for names in possible_opcodes ]

    assert len(edges) == 16, len(edges)
    for i,e in enumerate(edges):
        print(i, e)

    associated_opcodes = [ None ] * 16
    for moi, eux in enumerate(bipartite_perfect_matching(edges)):
        associated_opcodes[eux] = op_id_to_name[moi]
    print(associated_opcodes)
    print(list(op_name_to_id[i] for i in associated_opcodes))

    if False:
        for c, e in zip(associated_opcodes, edges):
            assert c in e, '{} not in {}'.format(c, e)

    return associated_opcodes2





if __name__ == '__main__':
    possible_opcodes = parse_data()
    print('possible_opcodes')
    try:
        for i, names in sorted(possible_opcodes.items()):
            print(i, names)
    except:
        for i, names in enumerate(possible_opcodes):
            print(i, names)



    print('perfect_matching_by_peeling')
    op_codes_by_id = perfect_matching_by_peeling(possible_opcodes)
    print(op_codes_by_id)
    print([ op_name_to_id[i] for i in op_codes_by_id])

    if True:
        print('bipartite_perfect_matching')
        test = match_opcodes(possible_opcodes, opcodes)

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
