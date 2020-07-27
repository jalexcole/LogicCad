import Logic
import processors
import unittest

class Test6502(unittest.TestCase):
    def testBasic(self):
        processor = processors.MOS6502()
        processor.ready = True
        address_bus = Logic.Bus(16)
        data_bus = Logic.Bus(8)
        memory = Logic.Memory(256, 8)


if __name__ == "__main__":
    unittest.main()