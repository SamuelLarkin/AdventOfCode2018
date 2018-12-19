#!/usr/bin/env python3

from __future__ import print_function

from computer import Computer





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        computer = Computer()
        computer.load_instructions(f)
        assert len(computer.instructions) == 36

    computer.compute()
    print('Answer:', computer.registers[0])
