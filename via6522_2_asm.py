class via6522(object):


    def __init__(self,porta="$6001",portb="$6000",ddra="$6003",ddrb="$6002"):
        self.porta = porta;
        self.portb = portb;
        self.ddra = ddra;
        self.ddrb = ddrb;

    def getPorta(self):
        return self.littleEndianness(self.porta);

    def getPortb(self):
        return self.littleEndianness(self.portb);

    def getDdra(self):
        return self.littleEndianness(self.ddra);

    def getDdrb(self):
        return self.littleEndianness(self.ddrb);

    def littleEndianness(self,s):
        all = s[1:]
        half0=all[2:]
        half1=all[:2]
        return half0+half1
