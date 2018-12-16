#!/usr/bin/env python

from __future__ import print_function

from opcodes import opcodes
import json
from utils import parse_data
from utils import SetEncoder



if __name__ == '__main__':
    possible_opcodes = parse_data()

    # [Matching (graph theory)](https://en.wikipedia.org/wiki/Matching_(graph_theory))
    if False:
        ass = [-1] * len(ops) # their number -> my number
        def assign(v):
            import random
            w = random.choice(edges[v])
            u, ass[w] = ass[w], v
            if u != -1: assign(u)
        for i in range(len(ops)):
            assign(i)

    if False:
        op_name_to_id = { op_name: i for i, op_name in possible_opcodes.keys() }
        edges = [ { op_name_to_id[n] } for names in possible_opcodes.values() ]
        import random
        ass = [-1]*len(ops) # their number -> my number
        for v in range(len(ops)):
            while v != -1:
                w = random.choice(edges[v])
                v, ass[w] = ass[w], v


    op_codes_by_id = [None] * 16
    # Let's add op_id to opcodes
    while len(possible_opcodes) > 0:
        op_id, op_name = min(possible_opcodes.items(), key=lambda x: len(x[1]))

        assert len(op_name) == 1, op_name
        op_name = op_name.pop()
        print(op_id, op_name)
        op_codes_by_id[op_id] = opcodes[op_name]

        del(possible_opcodes[op_id])
        for a, b in possible_opcodes.items():
            b -= {op_name}
        for op_id, names in list(filter(lambda x: len(x[1]) == 0, possible_opcodes.items())):
            del(possible_opcodes[op_id])
        print('possible_opcodes:', len(possible_opcodes), json.dumps(possible_opcodes, indent=3, cls=SetEncoder))
    print(op_codes_by_id)


    # Run the program.
    with open('data.b.txt', 'r') as f:
        registers = [0] * 4
        for l in f:
            instruction = list(map(int, l.strip().split()))
            op_codes_by_id[instruction[0]](instruction, registers)

    print('Answer:', registers[0])
    # 600
