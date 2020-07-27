class Memory:
    def __init__(self, size, bits):
        self.bits = bits
        self.size = size
        self.address = 0
        self.data = 0
        self.info = []
        

    def allacate_array(self):
        for i in range(0, size):
            self.info.append(0x0)

    def write(self):
        self.info[self.address] = self.data


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
        self.value = hex(2 ** self.length * 0)

    def read(self):
        pass
    def write(self):
        pass

    def overflow_check(self):
        while self.value > hex(2 ** self.length):
            self.value - hex(2 ** self.length + 1)

class Rom(Memory):
    def __init__(self):
        pass

class LogicChip:
    def __init__(self):
        self.type = None
        self.size = None

class Alu:
    def __init__(self):
        pass
    