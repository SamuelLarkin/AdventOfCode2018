#!/usr/bin/env python3
'''
'''

from __future__ import print_function

from computer import Computer





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        computer = Computer()
        computer.load_instructions(f)
        assert len(computer.instructions) == 31

    answer = 13970209
    computer.registers[0] = answer
    computer.compute()
    #print('Answer:', computer.registers[0])

    print('Answer:', answer)
    # 363 = 2^16 - 65899  TOO LOW
    # 13970209 because the only instruction involving the only register we can
    # play with is `eqrr 2 0 3` thus looking at the output of a run we see 
    #[364, 1, 13970209, 1, 27, 1]
    #eqrr 2 0 3
    # Thus, we conclude that register 0 should be equal to register 2 aka 13970209
