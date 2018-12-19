from utils import parse



class Computer:
    def __init__(self, register_size=6):
        self.registers = [0] * register_size
        self.instructions = None
        self.ip = None


    def load_instructions(self, f):
        self.ip, self.instructions = parse(f)


    def step(self):
        assert self.ip != None, 'You must load first.'
        assert self.instructions != None, 'You must load first.'

        # It updates register 0 to the current instruction pointer value.
        self.registers[0] = self.ip
        # Run the instruction
        #op = self.instructions[self.ip]
        #op.op_func(op.args, self.registers)
        self.instructions[self.ip](self.registers)
        # Sets the instruction pointer to the value of register 0.
        self.ip = self.registers[0]
        # Then adds one to the instruction pointer.
        self.ip += 1

        return self.ip < len(self.instructions)


    def compute(self):
        while self.step():
            #print('.', sep='', end='')
            print(self.registers)
            pass
