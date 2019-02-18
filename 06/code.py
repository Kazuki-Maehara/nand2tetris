#! /usr/bin/env python3
# coding = utf-8

#This is a coding program about binary.


_DestTable = {"null":"000", "M":"001", "D":"010", "MD":"011",
    "A":"100", "AM":"101", "AD":"110", "AMD":"111"}

def dest(dest_mnic):
    return _DestTable[dest_mnic] 

_CompTable = {"0":"0101010", "1":"0111111", "-1":"0111010",
    "D":"0001100", "A":"0110000", "!D":"0001101",
    "!A":"0110001", "-D":"0001111", "-A":"0110011",
    "D+1":"0011111", "A+1":"0110111", "D-1":"0001110",
    "A-1":"0110010", "D+A":"0000010", "D-A":"010011",
    "A-D":"0000111", "D&A":"0000000", "D|A":"0010101",
    "M":"1110000", "!M":"1110011", "M+1":"1110111",
    "M-1":"1110010", "D+M":"1000010", "D-M":"1010011",
    "M-D":"1000111", "D&M":"1000000", "D|M":"1010101"}

def comp(comp_mnic):
    return _CompTable[comp_mnic]


_JumpTable = ["null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]

def jump(jump_mnic):
    return bin(_JumpTable.index(jump_mnic))[2:].zfill(3)

