class Code:
    # A/M register replaced with X to allow register-independent lookup
    _compLookup = {
        '0':    '101010',
        '1':    '111111',
        '-1':   '111010',
        'D':    '001100',
        'X':    '110000',
        '!D':   '001101',
        '!X':   '110001',
        '-D':   '001111',
        '-X':   '110011',
        'D+1':  '011111',
        'X+1':  '110111',
        'D-1':  '001110',
        'X-1':  '110010',
        'D+X':  '000010',
        'D-X':  '010011',
        'X-D':  '000111',
        'D&X':  '000000',
        'D|X':  '010101'
    }

    _destLookup = {
        '':     '000',
        'M':    '001',
        'D':    '010',
        'DM':   '011',
        'MD':   '011',
        'A':    '100',
        'AM':   '101',
        'AD':   '110',
        'ADM':  '111',
        'AMD':  '111'
    }

    _jumpLookup = {
        '':     '000',
        'JGT':  '001',
        'JEQ':  '010',
        'JGE':  '011',
        'JLT':  '100',
        'JNE':  '101',
        'JLE':  '110',
        'JMP':  '111'
    }

    def __init__(self):
        pass
    
    def _dest(self, destStr):
        return Code._destLookup[destStr]
    
    def _comp(self, compStr):
        return ('1' if 'M' in compStr else '0') + Code._compLookup[compStr.replace('A', 'X').replace('M', 'X')]
    
    def _jump(self, jumpStr):
        return Code._jumpLookup[jumpStr]
    
    def encode(self, destStr, compStr, jumpStr):
        return '111' + self._comp(compStr) + self._dest(destStr) + self._jump(jumpStr)
