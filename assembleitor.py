from via6522_2_asm import via6522
from reset import rst
from lcd_2_asm import lcd


def main():
    via = via6522();
    resetall =rst();
    display = lcd(via.getPorta(),via.getPorta(),via.getDdra(),via.getDdrb());

    print(via.getPorta());
    print(via.getPortb());
    print(via.getDdra());
    print(via.getDdrb());
    print(resetall.reset());
    display.initilializeLcd();
    print (display.getBin());
    


if __name__ == "__main__":
    main()