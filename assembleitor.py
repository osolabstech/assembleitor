from via6522_2_asm import via6522
from reset import rst
from lcd_2_asm import lcd
from util6502 import utilities6502

def buildAsmCode():
    util = utilities6502();
    via = via6522();
    resetall =rst();
    util.string2bytearray("A9B6");
    display = lcd(via.getPorta(),via.getPorta(),via.getDdra(),via.getDdrb());
    asmCode = "";
    asmCode += resetall.reset();
    display.initilializeLcd();
    asmCode += display.getBin();
    util.saveBinFile(asmCode=asmCode,filename="code.bin",filesize=32768);
    # asmCodeByte=bytes.fromhex(asmCode);
    # print (asmCode);
    # print(asmCodeByte);
    # with open("code.bin","wb") as out_file:
    #  out_file.write(asmCodeByte);



def main():
    buildAsmCode();
    


if __name__ == "__main__":
    main()