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

    computer.registers[0] = 123
    computer.compute()
    #print('Answer:', computer.registers[0])

    answer = None
    print('Answer:', answer)
    # 16777215 too high


# [I made an ElfCode decompiler in Rust](https://www.reddit.com/r/adventofcode/comments/a8dkz2/2018_days_16_19_21_i_made_an_elfcode_decompiler/)
'''
     b = 123;
     do {
         b &= 0x1c8;
     } while b != 72;
     b = 0;
     do {
         c = b | 0x10000;
         b = 2238642;   # 0x2228B2
 8:      f = c & 0xff;
         b += f;
         b &= 0xffffff;
         b *= 65899;   # 1016B
         b &= 0xffffff;
         if 256 <= c {
             f = 0;
18:          e = f + 1;
             e *= 256;
             if e <= c {
                 f += 1;
                 goto 18;
             }
             c = f;
             goto 8;
         }
     } while b != a;
'''
