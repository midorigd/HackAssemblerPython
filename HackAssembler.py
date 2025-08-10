from src.Assembler import HackAssembler

import sys

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print('Usage: python3 -m HackAssembler filename.asm')
        return

    assembler = HackAssembler()
    assembler.assembleProgram(filename)

main()
