class utilities6502(object):

    def __init__(self):
        self.bin = "";
 
    def string2bytearray(self,s="",sizebyte=32768):
        b = bytearray([0xea] *sizebyte); # create an array of 32768 ea
        stop = len(s);
        
        for letter in s:
            print(letter);
        return b

    def littleEndianness(self,s):
        all = s[1:]
        half0=all[2:]
        half1=all[:2]
        return half0+half1



    def saveBinFile(self,asmCode="",filename="code.bin",filesize=32768,irq="$8000",reset="$8000",nmi="$8000"):
        asmCodeByte=bytearray.fromhex(asmCode); #asmCode < 16384 if not it fails fromhex()
        print(len(asmCodeByte));
        bytePad=bytearray([0x00] * (filesize - len(asmCodeByte)-6));
        irqB=bytearray.fromhex(self.littleEndianness(irq));
        bytePad.extend(irqB);
        resetB=bytearray.fromhex(self.littleEndianness(reset));
        bytePad.extend(resetB);
        nmiB=bytearray.fromhex(self.littleEndianness(nmi));
        bytePad.extend(nmiB);
        asmCodeByte.extend(bytePad);
        print(len(asmCodeByte));
        with open(filename,"wb") as out_file:
          out_file.write(asmCodeByte);

# rom[0] = 0xa9 # LDA 6502 machine instruction for LDA #$42 # for literal number and $ to encode as hexadecimal
# rom[1] = 0x42 # hexadecimal number 42

# rom[2] = 0x8d # STA to memory expects 3 bytes total (instruction +low address + high address)
# rom[3] = 0x00 # low address
# rom[4] = 0x60 # high address

# #tell the procesor to fetch first instrucion at 8000 (0000 of the actual eprom but with A15 enabled it would look at 8000)
# rom[0x7ffc] = 0x00 # low byte that will be read as FFFC
# rom[0x7ffd] = 0x80 # high byte that will be read as FFFD
# with open("rom006.bin","wb") as out_file:
#     out_file.write(rom)


