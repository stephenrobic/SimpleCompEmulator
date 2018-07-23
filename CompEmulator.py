import binascii
import sys

class Narc:
    def __init__(self, instruction_list = [], memory= [0]*64000, run= True, PC= 0, ACC= 0, INDEX = [0]*3): 
        self.instruction_list = instruction_list
        self.memory = memory
        self.run = run
        self.PC = PC
        self.ACC = ACC
        self.INDEX = INDEX

        self.instruction = {
        0:'HLT',
        1:'LDA',
        2:'STA',
        3:'ADD',
        4:'TCA',
        5:'BRU',
        6:'BIP',
        7:'BIN',
        8:'RWD',
        9:'WWD',
        10:'SHL',
        11:'SHR',
        12:'LDX',
        13:'STX',
        14:'TIX',
        15:'TDX'
        }

    def Get_Binary_Words(self):
        self.file_name = sys.argv[1]

        with open(self.file_name, 'rb') as f: #read binary file
            #TOD: Make this read file to the last line, not just specified range!!!
            for x in range(0,70,2): #traverse 2 bytes at a time (16 bits) for each output line
                #Seek position and read N bytes
                f.seek(x)  # Go to every next 2nd position for every iteration
                self.couple_bytes = f.read(2) #read the 2 bytes at once
                self.hexdata = binascii.hexlify(self.couple_bytes) #translate to hex
                self.bindata = (bin(int(self.hexdata, 16)))[2:].zfill(16) #int(data,baseThatItsIn) #.zfill fills with zeros before
                self.instruction_list.append(self.bindata)

    def Process_Instruction_Word(self, word):
        self.opcode = word
        self.opcode = int(str(self.opcode)[:-12])
        self.opcode = int(str(self.opcode),2)
        self.indirect_flag = word
        self.indirect_flag = str(self.indirect_flag)[:-10]
        self.indirect_flag = str(self.indirect_flag)[5:]
        self.indirect_flag = int(self.indirect_flag)
        self.index_flag = word
        self.index_flag = str(self.index_flag)[:-7]
        self.index_flag = str(self.index_flag)[7:]
        self.index_flag = int(self.index_flag,2)
        self.address = word
        self.address = str(self.address)[8:]
        self.address = int(self.address,2)
        self.i = self.instruction[self.opcode]

        self.PC += 1

        if self.i == 'HLT':
            self.run = False

        elif self.i == 'LDA':
            self.ACC = self.memory[self.address]
            
        elif self.i == "STA":
            self.memory[self.address] = self.ACC
           
        elif self.i == "ADD":
            self.ACC += self.memory[self.address]

        elif self.i == "TCA":
            self.ACC_temp = bin(self.ACC)[2:].zfill(16)
            self.ACC = -self.ACC
            
        elif self.i == "BRU":
            self.PC = self.address
            
        elif self.i == "BIP":
            if self.ACC > 0:
                self.PC = self.address

        elif self.i == "BIN":
            if self.ACC < 0:
                self.PC = self.address

        elif self.i == "RWD":
            self.in_word = int(input("?"))
            self.ACC = self.in_word

        elif self.i == "WWD":
            print(self.ACC)

        elif self.i == "SHL":
            self.ACC = self.ACC << 1

        elif self.i == "SHR":
            self.ACC = self.ACC >> 1

        elif self.i == "LDX":
            self.INDEX[self.index_flag] = self.memory[self.address]

        elif self.i == "STX":
            self.memory[self.address] = self.INDEX[self.index_flag]

        elif self.i == "TIX":
            self.INDEX[self.index_flag] = self.INDEX[self.index_flag] + 1 
            if INDEX[self.index_flag] == 0:
                self.PC = self.address

        elif self.i == "TDX":
            self.INDEX[self.index_flag] = self.INDEX[self.index_flag] - 1
            if self.INDEX[self.index_flag] != 0:
                self.PC = self.address

        else:
            print ("Out of 16 bit range")

    def fetch_and_execute(self):
        self.Get_Binary_Words()
        self.memory[34] = 1
        while self.run == True:
            self.binary_string = self.instruction_list[self.PC]
            self.Process_Instruction_Word(self.binary_string)

def main():
    narc = Narc()
    print('==================Beginning execution====================')
    narc.fetch_and_execute()
    print('=======================Done==============================')
    
main()
