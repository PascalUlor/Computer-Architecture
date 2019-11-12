"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # pass
        self.ram = [0]*256
        self.reg = [0]*8
        self.pc = 0

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, data):
        self.ram[address] = data

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram_write(address, instruction)
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # pass
        # decalre operands
        LDI = 0b10000010
        PRN= 0b01000111
        HLT = 0b00000001

        IR = self.ram_read(self.pc)
        operand_a = self.ram_read(self.pc + 1)
        operand_b = self.ram_read(self.pc + 2)
        print('==RAM=',self.ram)
        print('==b=',operand_b)
        print('==a=',operand_a)
        
        running = True
        while running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # Read from ram to check values in address ram.read()
            if IR == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3 # move to next MAR
            elif IR == PRN:
                print(self.reg[operand_a])
                self.pc += 2
            elif IR == HLT:
                running = False