#! /usr/bin/env python3
# coding = utf-8

import parser, code, sys, SymbolTable, re
filename = sys.argv[1]
fnameLen = len(filename)

prsInstance =  parser.Parser(filename)
stInstance = SymbolTable.SymbolTable()
bin_codes = []


def writeBinFile():
    bin_str = '\n'.join(bin_codes)

    f = open(sys.argv[1][0 : fnameLen - 4] + '.hack', 'w')
    f.write(bin_str)
    f.close()



#Pass-1
lineCnt = 0

while 1:
    if (prsInstance.commandType() == "A_COMMAND") or (prsInstance.commandType() == "C_COMMAND"):
        lineCnt += 1
        prsInstance.advance()

    elif (prsInstance.commandType() == "L_COMMAND"):
        stInstance.addEntry(prsInstance.symbol(), lineCnt)
        prsInstance.advance()
    else:
        prsInstance.advance() 

    if prsInstance.hasMoreCommands():
        pass
    else :
        break


symAddress = 16
prsInstance.__init__(filename)


while 1:
    if prsInstance.commandType() == "A_COMMAND":
        #print("a command")
        if re.findall(r'^[0-9]+', prsInstance.symbol()):
            #print("case of digits")
            A_binLine = bin(int(prsInstance.symbol()))[2:].zfill(16)
            #write to a .hack file
        else:
            if prsInstance.symbol() in stInstance.symbolTable:
                #print("case :  symbol is in symboltable") 
                address = stInstance.symbolTable[prsInstance.symbol()]
                A_binLine = bin(address)[2:].zfill(16)
            else:
                #print("case : symbol is not in symboltable!!!!")
                stInstance.addEntry(prsInstance.symbol(), symAddress)
                A_binLine = bin(symAddress)[2:].zfill(16)
                symAddress += 1
        bin_codes.append(A_binLine)
        print(A_binLine)
        prsInstance.advance()
        


    elif prsInstance.commandType() == "L_COMMAND":
        prsInstance.advance()
        #just advance the line-list of parse-instance.

    elif prsInstance.commandType() == "C_COMMAND":
        print("c command")
        dest_mnic = prsInstance.dest()
        dest_bin = code.dest(dest_mnic)
        
        comp_mnic = prsInstance.comp()
        comp_bin = code.comp(comp_mnic)
        
        jump_mnic = prsInstance.jump()
        jump_bin = code.jump(jump_mnic)
        
        C_binLine = "111" + comp_bin + dest_bin + jump_bin
        bin_codes.append(C_binLine)
        print(C_binLine)
        prsInstance.advance()


    elif prsInstance.commandType() == "COMMENT":
        #print("This is a comment")
        prsInstance.advance()

    elif prsInstance.commandType() == "BLANK":
        #print("This is a blank")
        prsInstance.advance()
    
    if prsInstance.hasMoreCommands():
        pass
    else :
        break

print(stInstance.symbolTable)

writeBinFile()
