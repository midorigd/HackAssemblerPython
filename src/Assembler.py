from src.SymbolTable import SymbolTable
from src.Code import Code
from src.Parser import Parser

class HackAssembler:
    def __init__(self):
        self._symbolTable = SymbolTable()

    def _lookupAddress(self, symbol):
        # symbol is a constant
        if symbol.isdigit():
            return f'{int(symbol):016b}'

        # symbol is predefined or label from pass 1
        if self._symbolTable.contains(symbol):
            return f'{self._symbolTable.getAddress(symbol):016b}'

        # symbol is a variable: needs to be added to symbolTable
        addr = self._symbolTable.addEntry(symbol)
        return f'{addr:016b}'

    # PASS 1: process and add labels to symbol table
    def _pass1(self, assemblyFile):
        self._parser = Parser(assemblyFile)
        lineCount = 0
        
        while self._parser.hasMoreCommands():
            self._parser.advance()

            if self._parser.commandType() == 'L_COMMAND':
                self._symbolTable.addEntry(self._parser.symbol(), lineCount)
            else:
                lineCount += 1

    # PASS 2: process and convert each line into binary depending on command type
    def _pass2(self, binaryFile):
        outFile = open(binaryFile, 'w')

        # Reset parser line position, initialize Code module
        self._parser.reset()
        code = Code()

        while self._parser.hasMoreCommands():
            self._parser.advance()

            if self._parser.commandType() == 'A_COMMAND':
                print(self._lookupAddress(self._parser.symbol()), file=outFile)

            elif self._parser.commandType() == 'C_COMMAND':
                print(code.encode(self._parser.dest(), self._parser.comp(), self._parser.jump()), file=outFile)

        outFile.close()

    # Drives the assembly process
    def assembleProgram(self, inFile):
        outFile = f'{inFile.rstrip('.asm')}.hack'

        self._pass1(inFile)
        self._pass2(outFile)
