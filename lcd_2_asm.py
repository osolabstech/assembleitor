import random

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

    def fillRandomLine(self,lenght=20,pattern=["/","\\"],patternLcd=[0x2f,0xfa]):
        line=[];
        lineLcd=[];
        for position in range(0,lenght):
            r=random.randrange(0,2);
            line.append(pattern[r]); #includes 0 and 1 but not 2
            lineLcd.append(patternLcd[r]);
        return line,lineLcd

    def displayLinesLcd(self,lineMatrix=[]):
        for line in lineMatrix:
            print(''.join(line));
        #the final one instead of printing a pattern will generate the assembler code to display each line
    
    def displayLinesLcdWindow(self,lineMatrix=[],startWindow=0,linesWindow=4):
        for line in range(startWindow,startWindow+linesWindow):
            print(''.join(lineMatrix[line]));
        #the final one instead of printing a pattern will generate the assembler code to display each line

    def tenPrintline(self,lenght=20,lines=4,allLines=6):
        lineMatrix=[];
        lineMatrixLcd=[];
        for i in range(0,allLines):
            line,lineLcd=self.fillRandomLine(lenght);
            lineMatrix.append(line);
            lineMatrixLcd.append(lineLcd);
        for startWindow in range(0,allLines-lines):
            self.displayLinesLcdWindow(lineMatrix,startWindow,lines);

    

