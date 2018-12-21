from utils import parse



class Computer:
    def __init__(self, register_size=6):
        self.registers = [0] * register_size
        self.instructions = None
        self._register0 = None
        self.ip = 0
        self.instruction_pointer = 0


    @property
    def register0(self):
        return self.registers[self._register0]

    @register0.setter
    def register0(self, value):
        self.registers[self._register0] = value

    def load_instructions(self, f):
        self._register0, self.instructions = parse(f)


    def step(self):
        assert self._register0 != None, 'You must load first.'
        assert self.instructions != None, 'You must load first.'

        # It updates register 0 to the current instruction pointer value.
        self.register0 = self.ip
        # Run the instruction
        #op = self.instructions[self.ip]
        #op.op_func(op.args, self.registers)
        print(self.instructions[self.ip].name, ' '.join(map(str, self.instructions[self.ip].args)))
        self.instructions[self.ip](self.registers)
        # Sets the instruction pointer to the value of register 0.
        self.ip = self.register0
        # Then adds one to the instruction pointer.
        self.ip += 1

        return self.ip < len(self.instructions)


    def compute(self):
        while self.step():
            #print('.', sep='', end='')
            print(self.registers)
            pass
