opcodes = {}

########################################
# Addition
def addr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] + registers[B]
opcodes['addr'] = addr



def addi(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] + B
opcodes['addi'] = addi



########################################
# Multiplication
def mulr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] * registers[B]
opcodes['mulr'] = mulr



def muli(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] * B
opcodes['muli'] = muli



########################################
# Bitwise AND
def banr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] & registers[B]
opcodes['banr'] = banr



def bani(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] & B
opcodes['bani'] = bani



########################################
# Bitwise OR
def borr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] | registers[B]
opcodes['borr'] = borr



def bori(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A] | B
opcodes['bori'] = bori



########################################
# Assignment
def setr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = registers[A]
opcodes['setr'] = setr



def seti(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = A
opcodes['seti'] = seti



########################################
# Greater-than testing
def gtir(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if A > registers[B] else 0
opcodes['gtir'] = gtir



def gtri(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if registers[A] > B else 0
opcodes['gtri'] = gtri



def gtrr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if registers[A] > registers[B] else 0
opcodes['gtrr'] = gtrr



########################################
# Equality testing
def eqir(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if A == registers[B] else 0
opcodes['eqir'] = eqir



def eqri(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if registers[A] == B else 0
opcodes['eqri'] = eqri



def eqrr(opcode, registers):
    assert len(opcode) == 4
    assert len(registers) == 4
    O, A, B, C = opcode
    registers[C] = 1 if registers[A] == registers[B] else 0
opcodes['eqrr'] = eqrr



assert len(opcodes) == 16, len(opcodes)
assert len(set(opcodes.values())) == 16, 'at least two opcodes have the same function.'
