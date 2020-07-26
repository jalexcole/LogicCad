class Memory:
    def __init__(self, size, bits):
        self.bits = bits
        self.size = size
        self.address = None
        self.data = None
    def allacate_array(self):
        pass
    def write(self):

class Register:
    def __init__(self, size):
        self.size = size
        self.type = "Gerneral"
    def read(self):
        pass
    def write(self):
        pass

class Bus:
    def __init__(self, length):
        self.length = length
    def read(self):
        pass
    def write(self):
        pass

class Rom(Memory):
    def __init__(self):
        pass

class LogicChip:
    def __init__(self):
        self.type = None
        self.size = None
    