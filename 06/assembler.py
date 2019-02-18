#! /usr/bin/env python3
# coding = utf-8

import parser, code, sys
filename = sys.argv[1]
fnameLen = len(filename)

prsInstance =  parser.Parser(filename)
bin_codes = []


def writeBinFile():
    bin_str = '\n'.join(bin_codes)

    f = open(sys.argv[1][0 : fnameLen - 4] + '.hack', 'w')
    f.write(bin_str)
    f.close()


while 1:
    if prsInstance.commandType() == "A_COMMAND":
        A_binLine = bin(int(prsInstance.symbol()))[2:].zfill(16)
        bin_codes.append(A_binLine)
        print(A_binLine)
        prsInstance.advance()
        #write to a .hack file

    elif prsInstance.commandType() == "L_COMMAND":
        pass

        #try to write the program when I reach the next step (symbolic table)

    elif prsInstance.commandType() == "C_COMMAND":
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


writeBinFile()
