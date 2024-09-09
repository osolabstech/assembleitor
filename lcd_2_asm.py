class lcd(object):


    def __init__(self,porta,portb,ddra,ddrb):
        self.porta = porta;
        self.portb = portb;
        self.ddra = ddra;
        self.ddrb = ddrb;
        # ;define LCD signals
        # E = %10000000 ;Enable Signal
        self.e= "80";
        # RW = %01000000 ; Read/Write Signal
        self.rw = "40";
        # RS = %00100000 ; Register Select
        self.rs="20";
        self.bin="";

    def littleEndianness(self,s):
        all = s[1:]
        half0=all[2:]
        half1=all[:2]
        return half0+half1

    def initilializeLcd(self):
        #   ;BEGIN Initialize LCD Display
        #   ;set all port B pins as output
        #   lda #%11111111  ;load all ones equivalent to $FF
        self.bin +="A9FF";
        #   sta DDRB ;store the accumulator in the data direction register for Port B
        self.bin +="8D";
        self.bin +=self.ddrb;
        #   lda #%11111111  ;set all pins as output
        self.bin +="A9FF";
        #   sta DDRA ;store the accumulator in the data direction register for Port A
        self.bin +="8D";
        self.bin +=self.ddra;
        #   ;END Initialize LCD Display
    
    def getBin(self):
        return self.bin
