import re

class Parser:
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

    @property
    def _eqPos(self):
        return self._current.find('=')

    @property
    def _scPos(self):
        try:
            return self._current.index(';')
        except ValueError:
            return len(self._current)

    @property
    def _destStr(self):
        if self._eqPos == -1:
            return ''
        
        return self._current[:self._eqPos]

    @property
    def _compStr(self):
        return self._current[self._eqPos + 1 : self._scPos]

    @property
    def _jumpStr(self):
        return self._current[self._scPos + 1:]

    def hasMoreCommands(self):
        return self._pos < len(self._contents) - 1

    def advance(self):
        self._pos += 1

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

    def dest(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have dest segment')
        
        return self._destStr

    def comp(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have comp segment')
        
        return self._compStr

    def jump(self):
        if self.commandType() != 'C_COMMAND':
            raise TypeError(f'Type {self.commandType()} does not have jump segment')
        
        return self._jumpStr
