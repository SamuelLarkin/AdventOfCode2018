from collections import namedtuple
from opcodes import opcodes
import re


InstructionBase = namedtuple('InstructionBase', ('id', 'name', 'func', 'args'))
class Instruction(InstructionBase):
    def __call__(self, registers):
        self.func(self.args, registers)



def parse(f):
    # TODO: use re, it is more robust
    ##ip 2
    #addi 2 16 2
    #seti 1 1 3
    ip_re = re.compile(r'#ip (\d+)')
    op_re = re.compile(r'(\w{4}) (\d+) (\d+) (\d+)')
    f = iter(f)
    m = ip_re.match(next(f).strip())
    assert m, m.group(0)
    ip = int(m.group(1))

    instructions = []
    for i, l in enumerate(f):
        m = op_re.match(l)
        assert m, m.group(0)
        op_name = m.group(1)
        args = [ int(a) for a in m.group(2,3,4) ]
        instructions.append(Instruction(id=i, name=op_name, func=opcodes[op_name], args=args))

    return ip, instructions
