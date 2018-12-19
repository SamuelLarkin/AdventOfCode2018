from computer import Computer
from utils import parse
import re
import unittest



test_data = '''
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
'''
test_data = test_data.strip().split('\n')
print(test_data)


test_instructions = '''
ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]
'''
test_instructions = test_instructions.strip().split('\n')
print(test_instructions)


class TestCompute(unittest.TestCase):
    def disabled(self):
        reader = re.compile(r'ip=(\d) \[(\d), (\d), (\d), (\d), (\d), (\d)\] (.+) (\d \d \d) \[(\d), (\d), (\d), (\d), (\d), (\d)\]')
        for l in test_instructions:
            m = reader.match(l.strip())
            assert m, l
            ip = m.group(1)
            before = m.group(2,3,4,5,6,7)
            op = m.group(8)
            args = m.group(9,10,11)
            #after = m.group(12,13,14,15,16,17)
            after = m.group(12)
            print(ip, before, op, args, after)


    def test0(self):
        computer = Computer()
        computer.load_instructions(test_data)

        ips = (0,1,2,4,6)
        before = ( [0, 0, 0, 0, 0, 0], [1, 5, 0, 0, 0, 0], [2, 5, 6, 0, 0, 0], [4, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 0], )
        after = ( [0, 5, 0, 0, 0, 0], [1, 5, 6, 0, 0, 0], [3, 5, 6, 0, 0, 0], [5, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 9], )

        self.assertListEqual(computer.registers, before[0])
        computer.step()
        self.assertListEqual(computer.registers, after[0])


    def test1(self):
        '''
        ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
        ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
        ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
        ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
        ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]
        '''
        computer = Computer()
        computer.load_instructions(test_data)
        ips = (0,1,2,4,6)
        before = ( [0, 0, 0, 0, 0, 0], [1, 5, 0, 0, 0, 0], [2, 5, 6, 0, 0, 0], [4, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 0], )
        after = ( [0, 5, 0, 0, 0, 0], [1, 5, 6, 0, 0, 0], [3, 5, 6, 0, 0, 0], [5, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 9], )
        for ip_ref, b_ref, a_ref in zip(ips, before, after):
            self.assertEqual(computer.ip, ip_ref)
            #self.assertListEqual(computer.registers, b_ref)
            computer.step()
            self.assertListEqual(computer.registers, a_ref)


    def test_full(self):
        '''
        ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
        ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
        ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
        ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
        ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]
        '''
        computer = Computer()
        computer.load_instructions(test_data)
        ips = (0,1,2,4,6)
        before = ( [0, 0, 0, 0, 0, 0], [1, 5, 0, 0, 0, 0], [2, 5, 6, 0, 0, 0], [4, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 0], )
        after = ( [0, 5, 0, 0, 0, 0], [1, 5, 6, 0, 0, 0], [3, 5, 6, 0, 0, 0], [5, 5, 6, 0, 0, 0], [6, 5, 6, 0, 0, 9], )
        computer.compute()
        print(computer.registers)
