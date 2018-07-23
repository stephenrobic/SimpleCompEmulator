Created an emulator for a simple computer which operates on 16-bit integers using Python. 
I used the binascii module for hexadecimal conversion and the sys module to open the input file as a command line argument.
The program reads a binary file containing 16 bit instructions words into an instruction list, and using direct addressing, from each word, 
it extracts certain bits and translates the word into one of 15 assembly language instructions.
With 8 bits of each word being used in the memory address representation, this program directly addresses only 256 memory locations. 
t also makes use of a program counter and accumulator. For future implementation, bits are also extracted for an index flag, indirect flag, 
and a single opcode extension bit.

The program must be run through the command line, with the second argument being the file to emulate.

Contained in this repository, is a Divide.bin file, which acts as a simple division calculator utilizing the emulator.