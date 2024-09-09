from via6522_2_asm import via6522
from reset import rst
from lcd_2_asm import lcd

def buildAsmCode():
    via = via6522();
    resetall =rst();
    display = lcd(via.getPorta(),via.getPorta(),via.getDdra(),via.getDdrb());
    asmCode = "";
    asmCode += resetall.reset();
    display.initilializeLcd();
    asmCode += display.getBin();
    print (asmCode);



def main():
    buildAsmCode();
    


if __name__ == "__main__":
    main()