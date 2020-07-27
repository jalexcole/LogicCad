"""
This is a python based 65c02 assembler that can take 65c02 assembly files and transalte them into comma seperated hex files
"""
import sys

def main():
    table = {
        "BRK i": 0x00, "ORA x": 0x01, "ORA zp": 0x05, "ASL zp": 0x06, "PHP i": 0x08, "ORA #": 0x09, "ORA a": 0x0D, "ASL a": 0x0E
        "BPL r": 0x10, "ORA y": 0x11, "ORA x": 0x15, "ASL x": 0x16, "CLC i": 0x18, "ORA a,y": 0x19, "ORA a,x": 0x1D, "ASL a,x": 0x1E
        "JSR a": 0x20, "AND" : 0x21, "BIT zp": 0x24, "AND zp":0x15, "ROL zp": 0x26, "PLP i" 0x28, "AND #": 0x29, "ROL a": 0x2A, "BIT A": 0x2C, "AND a": 0x2D, "ROL a": 0x2E,
        "BMI r": 0x30, "AND y": 0x31, "And zp,x": 0x35, "ROL zp,x": 0x36, "SEC i": 0x38, "AND a,y": 0x39, "AND a,x": 0x3D, "ROL a,x": 0x3E
    }
def flip_endiness(value):
    pass

if __name__ == "__main__":
    main()