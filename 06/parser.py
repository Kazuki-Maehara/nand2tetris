#! /usr/bin/env python3
# coding =utf-8


#This is an assember program for Hack computer, about nand2tetris project

#Get a argv's list
import sys
argvs = sys.argv

#Import regular expression module
import re

class Parser(object):
    def __init__(self, filename):
        #Open the *.asm file and assign into the "lines" variance
        asm_file = open(filename, 'r')
        self.lines = asm_file.readlines()
        asm_file.close()

        self.linesLength = len(self.lines)
        self.line_num = 0 
        self.CurrentLine = self.lines[self.line_num]
        self.splitted = re.split(r'([@=;\n\(\)]\s*)', self.lines[self.line_num])

        print("Open file : {filename}\nTotal lines :{lenlines}".format(filename=filename,
            lenlines=len(self.lines)))

    def hasMoreCommands(self):
        if self.line_num + 1 > self.linesLength :
            return False
        else:
            return True


    def advance(self):
        self.line_num = self.line_num + 1
        
        if self.line_num >= self.linesLength:
            pass
        else:
            self.splitted = re.split(r'([@=;\n\(\)\s*])', self.lines[self.line_num])


    def commandType(self):
        if re.findall(r'^\s*//', self.lines[self.line_num]):
            return "COMMENT"
        elif re.findall(r'^\s*@', self.lines[self.line_num]):
            return "A_COMMAND"
        elif re.findall(r'^\s*\(.*\)', self.lines[self.line_num]):
            return "L_COMMAND"
        elif re.findall(r'\S+', self.lines[self.line_num]):
            return "C_COMMAND"
        else:
            return "BLANK"

    def symbol(self):
        #match = re.findall(r'[0-9a-zA-Z_.$:]*', self.lines[self.line_num])
        if "@" in self.splitted:
            symbol = self.splitted[self.splitted.index("@") + 1]
            return symbol
        elif "(" in self.splitted:
            symbol = self.splitted[self.splitted.index("(") + 1]
            return symbol

    def dest(self):
        if "=" in self.splitted:
            eq_index = self.splitted.index("=")
            return self.splitted[eq_index - 1]
        else:
            return "null"

    def comp(self):
        if "=" in self.splitted: 
            eq_index = self.splitted.index("=")
            return self.splitted[eq_index + 1]
        elif ";" in self.splitted:
            sc_index = self.splitted.index(";")
            return self.splitted[sc_index - 1]
        else:
            return self.splitted[0]

    def jump(self):
        if ";" in self.splitted: 
            sc_index = self.splitted.index(";")
            return self.splitted[sc_index + 1]
        else:
            return "null"
