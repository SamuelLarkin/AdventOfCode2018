import json
from collections import defaultdict
from copy import deepcopy
from opcodes import opcodes



# [How to JSON serialize sets?](https://stackoverflow.com/a/8230505)
class SetEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, set):
         return list(obj)
      return json.JSONEncoder.default(self, obj)



def parse_value(line):
    #Before: [2, 3, 2, 2]
    #After:  [2, 3, 4, 2]
    values = list(map(int, line.strip().split(' ', 1)[1].strip()[1:-1].split(',')))
    assert len(values) == 4

    return values



def parse_data(filename='data.a.txt'):
    #Before: [2, 3, 2, 2]
    #15 3 2 2
    #After:  [2, 3, 4, 2]
    #
    possible_opcodes = defaultdict(lambda: set())
    # Since we know in advance how many opcodes we have, we could use an array
    # instead of a hash but that would imply changing  our
    # perfect_matching_by_peeling() to work with array instead of hash.
    #possible_opcodes = [ set() for _ in range(16) ]
    with open('data.a.txt', 'r') as f:
        a = 0
        counts = [0] * 16
        for i, b in enumerate(f):
            before_ref = parse_value(b)
            op_code = list(map(int, f.readline().strip().split()))
            assert len(op_code) == 4
            after = parse_value(f.readline())
            f.readline()
            a += 1

            count = 0
            for op_name, op_func in opcodes.items():
                before = deepcopy(before_ref)
                op_func(op_code, before)
                if before == after:
                    count += 1
                    possible_opcodes[op_code[0]].add(op_name)

    print('Found {} samples'.format(a))

    return possible_opcodes
