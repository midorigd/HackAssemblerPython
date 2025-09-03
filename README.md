# HackAssembler (Python)

This is a Python implementation of the assembler for the Hack assembly language from project 6 of nand2tetris.

The assembler takes a single `.asm` file as a command-line argument and creates a `.hack` file with the corresponding machine language.

## Modules

HackAssembler: Program entry point  

Assembler: Drives the assembly process  
Code: Handles translation of C-commands  
Parser: Handles input filestream and categorizes commands  
SymbolTable: Tracks variable names and memory addresses  

## Building the project

Run the following from the terminal:

```zsh
git clone https://github.com/midorigd/HackAssemblerPython
cd HackAssemblerPython
```

## Running the project

Run the following from the project directory:

```zsh
python3 -m HackAssembler path/to/file.asm
```

## Notes

My C++ implementation of this project: [HackAssembler (C++)](https://github.com/midorigd/HackAssemblerCpp)

### Stats

275 lines (219 loc)

## References

[nand2tetris](https://www.nand2tetris.org/course)

