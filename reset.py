class rst(object):


    def __init__(self,org="$8000"):
        self.org = org;
        self.bin = "";

    def getOrg(self):
        return self.littleEndianness(self.org);

    def reset(self):
        #   ;BEGIN Initialize stack pointer to $01FF
        #   ldx #$ff 
        self.bin+= "A2FF"
        #   txs   ;transfer the X register to the Stack pointer
        self.bin+= "9A"
        #   ;END Initialize stack pointer to $01FF
        return self.bin;

    def littleEndianness(self,s):
        all = s[1:]
        half0=all[2:]
        half1=all[:2]
        return half0+half1