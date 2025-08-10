class SymbolTable:
    def __init__(self):
        self._nextAddress = 15
        self._symbolTable = {
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            
            'SCREEN': 16384,
            'KBD': 24576,
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4
        }

    def addEntry(self, symbol, address=None):
        if address is None:
            address = self.getNextFreeAddress()

        self._symbolTable[symbol] = address
        return address

    def contains(self, symbol):
        return symbol in self._symbolTable

    def getAddress(self, symbol):
        if symbol not in self._symbolTable:
            raise KeyError(f'Symbol {symbol} does not exist')
        
        return self._symbolTable[symbol]

    def getNextFreeAddress(self):
        self._nextAddress += 1
        return self._nextAddress
