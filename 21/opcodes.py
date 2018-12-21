num_args = 3
num_registers = 6
opcodes = {}

########################################
# Addition
def addr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] + registers[B]
opcodes['addr'] = addr



def addi(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] + B
opcodes['addi'] = addi



########################################
# Multiplication
def mulr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] * registers[B]
opcodes['mulr'] = mulr



def muli(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] * B
opcodes['muli'] = muli



########################################
# Bitwise AND
def banr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] & registers[B]
opcodes['banr'] = banr



def bani(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] & B
opcodes['bani'] = bani



########################################
# Bitwise OR
def borr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] | registers[B]
opcodes['borr'] = borr



def bori(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A] | B
opcodes['bori'] = bori



########################################
# Assignment
def setr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = registers[A]
opcodes['setr'] = setr



def seti(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = A
opcodes['seti'] = seti



########################################
# Greater-than testing
def gtir(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if A > registers[B] else 0
opcodes['gtir'] = gtir



def gtri(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if registers[A] > B else 0
opcodes['gtri'] = gtri



def gtrr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if registers[A] > registers[B] else 0
opcodes['gtrr'] = gtrr



########################################
# Equality testing
def eqir(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if A == registers[B] else 0
opcodes['eqir'] = eqir



def eqri(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if registers[A] == B else 0
opcodes['eqri'] = eqri



def eqrr(args, registers):
    assert len(args) == num_args
    assert len(registers) == num_registers
    A, B, C = args
    registers[C] = 1 if registers[A] == registers[B] else 0
opcodes['eqrr'] = eqrr



assert len(opcodes) == 16, len(opcodes)
assert len(set(opcodes.values())) == 16, 'at least two opcodes have the same function.'

op_id_to_name = list(opcodes.keys())
print('op_id_to_name:', op_id_to_name)

op_name_to_id = { op_name: i for i, op_name in enumerate(op_id_to_name) }
print('op_name_to_id:', op_name_to_id)
