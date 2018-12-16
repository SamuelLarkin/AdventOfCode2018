#!/usr/bin/env python

from __future__ import print_function

from opcodes import opcodes
from copy import deepcopy





def parse_value(line):
    #Before: [2, 3, 2, 2]
    return list(map(int, line.strip().split(' ', 1)[1].strip()[1:-1].split(',')))



if __name__ == '__main__':
    #Before: [2, 3, 2, 2]
    #15 3 2 2
    #After:  [2, 3, 4, 2]
    #
    counts = [0] * 16
    with open('data.a.txt', 'r') as f:
        for b in f:
            before_ref = parse_value(b)
            o = list(map(int, f.readline().strip().split()))
            after = parse_value(f.readline())
            f.readline()

            count = 0
            for op in opcodes.values():
                before = deepcopy(before_ref)
                op(o, before)
                count += int(before == after)
            counts[count] += 1

    assert counts[0] == 0, "It is suspicious that we have some examples that aren't match to any opcode."
    print(counts)
    print(counts[3:])
    print('Answer:', sum(counts[3:]))
    # 532 is too low
