import Logic

class MOS6502:
    def __init__(self):
        self.opcode = None
        # Input and Ouput
        self.address = 0x0000
        self.data = 0x00
        self.bus_enable = True
        self.interupt_request = None
        self.memory_lock = False
        self.nonmaskable_interupt = False
        self.phi2 = False
        self.phi2o = False
        self.phi10 = False
        self.no_connect = None
        self.rwb = True # Read/Write if True data is read, if False data is written
        self.ready = None
        self.reset = False
        self.set_overflow = False
        self.sync = False # SYNChronize with OpCode fetch
        self.vector_pull = False

        ## Status Flags
        self.negative = False
        self.overflow = False
        self.Break = False
        self.decimal = False
        self.interupt_disable = False
        self.zero = False
        self.carry = False

        ## Register lists
        self.x = 0x00
        self.y = 0x00
        self.instruction_register = None
        self.timing_control_unit = None
        self.alu = Logic.Alu()  # This may not be needed
        self.index_register = None
        self.accumulator_register = None
        self.processor_status_register = None
        self.program_counter_register = None
        self.stack_pointer_register = None

    # Load and Store operations
    def lda(self):
        """Load Accumulator with memmory"""
        self.rwb = True
        self.accumulator = self.data
        self.negative = True
        self.zero = True
    
    def ldx(self):
        """Load x register with memmory"""
        self.rwb = True
        self.x = self.data
        self.negative = True
        self.zero = True

    def ldy(self):
        """Load y register with memmory"""
        self.rwb = True
        self.y = self.data
        self.negative = True
        self.zero = True
        

    def sta(self):
        """Store Accumulator to memmory"""
        self.rwb = False # Enable Write out
        self.data = self.accumulator
        

    def stx(self):
        self.rwb = False # Enable Write out
        self.data = self.x

    def sty(self):
        self.rwb = False # Enable Write out
        self.data = self.y
    
    # Arrathmatic Operations
    def adc(self):
        new_accumulator = self.accumulator + self.data + self.carry
        self.negative = False
        if new_accumulator < self.accumulator:
            self.set_overflow = True
            self.carry = True
        if new_accumulator == self.accumulator:
            self.zero = True
        self.accumulator = new_accumulator

    def sbc(self):
        pass
    # Increment and Decrement
    def inc(self):
        pass
    def inx(self):
        pass
    def iny(self):
        pass
    def dec(self):
        pass
    def dex(self):
        pass
    def dey(self):
        pass
    
    # Shift and Rotate
    def asl(self):
        pass
    def lsl(self):
        pass
    def rol(self):
        pass
    def ror(self):
        pass

    # Logical Operations
    def AND(self):
        pass
    def ORA(self):
        pass
    def EOR(self):
        pass

    # Compare and Test bits
    def CMP(self):
        pass
    def CPX(self):
        pass
    def CPY(self):
        pass
    def BIT(self):
        pass

    # Branch
    def BCC(self):
        pass
    def BCS(self):
        pass
    def BNY(self):
        pass
    def BEQ(self):
        pass
    def BPL(self):
        pass
    def BMI(self):
        pass
    def BVC(self):
        pass
    def BVS(self):
        pass

    # Transfer
    def TAX(self):
        pass
    def TXA(self):
        pass
    def TAY(self):
        pass
    def TYA(self):
        pass
    def TSX(self):
        pass
    def TXS(self):
        pass

    # Stack
    def PHA(self):
        """Push Accumulator on Stack"""
        pass
    def PLA(self):
        """Pull Accumolator from Stack"""
        pass
    def PHP(self):
        """Push Processor Status on Stack"""
        pass
    def PLP(self):
        """Pull Processor Status from Stack"""
        pass

    # Subroutines and Jump
    def JMP(self):
        """ Does a flip - Please Recomment what this does
        Jump to new Location"""
        pass

    def JSR(self):
        """Jump to new location saving return address"""
        pass

    def RTS(self):
        """Return from subroutine"""
        pass

    def RTI(self):
        """ Return from Interups"""
        pass

    # Set and Clear
    def CLC(self):
        """Clear and Carry"""
        pass

    def SEC(self):
        """Set Carry Flag"""
        pass
    def CLD(self):
        """Clear Decimal Mode"""
        pass
    def SED(self):
        """Set Decimal Mode"""
        pass
    def CLI(self):
        """Clear Interupt Data Analysis"""
        pass
    def SEI(self):
        """Set Interupt Disabled Status"""
        pass
    def CLV(self):
        """Clear Overflow Flag"""
        pass
    # Miscilaneous
    def BRK(self):
        """Force an Interupt"""
        pass
    def NOP(self):
        """No Operation"""
        pass

