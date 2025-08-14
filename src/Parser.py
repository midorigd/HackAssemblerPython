import re

class Parser:
    compPattern = r'(?:([ADM]*)=)?([01AMD!\|&\-\+]*)(?:;([JGTEQLNMP]*))?'

    def __init__(self, filename):
        with open(filename) as file:
            self._contents = [trimLine for line in file.readlines() if (trimLine := Parser._removeComments(line)) != '']
        self._pos = -1

    @staticmethod
    def _removeComments(line):
        return re.sub(r'//.*', '', line.strip())

    @property
    def _current(self):
        return self._contents[self._pos]

    def splitCommand(self):
        matches = re.match(Parser.compPattern, self._current)
        self.dest = matches[1]
        self.comp = matches[2]
        self.jump = matches[3]

    def hasMoreCommands(self):
        return self._pos < len(self._contents) - 1

    def advance(self):
        self._pos += 1
        if self.commandType() == 'C_COMMAND':
            self.splitCommand()

    def reset(self):
        self._pos = -1

    def commandType(self):
        if self._current.startswith('@'):
            return 'A_COMMAND'
        
        if self._current.startswith('('):
            return 'L_COMMAND'
        
        return 'C_COMMAND'

    def symbol(self):
        if self.commandType() == 'C_COMMAND':
            raise TypeError('Type C_COMMAND does not have symbol')
        
        if self.commandType() == 'A_COMMAND':
            return self._current.lstrip('@')
        
        return self._current.lstrip('(').rstrip(')')

    @property
    def dest(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have dest segment')

        return self._dest
    
    @dest.setter
    def dest(self, val):
        if val is None:
            val = ''
        self._dest = val

    @property
    def comp(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have comp segment')

        return self._comp
    
    @comp.setter
    def comp(self, val):
        if val is None:
            val = ''
        self._comp = val

    @property
    def jump(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have jump segment')

        return self._jump
    
    @jump.setter
    def jump(self, val):
        if val is None:
            val = ''
        self._jump = val
