#!/usr/bin/env python

def execute_opcode(intcode,pointer):
    if intcode[pointer] == 1:
        intcode[pointer + 3 ] = int(intcode[pointer + 1]) + int(intcode[pointer + 2])
        status = True
    elif intcode[pointer] == 2:
        intcode[pointer +3 ] = int(intcode[pointer + 1]) * int(intcode[pointer + 2])
        status = True
    else
        status = False
    return intcode,pointer,status

input = open("intcode", "r")
intcode = input.split(",")
incode = [ int(x) for x in intcode ]
intcode[1] = 12
intcode[2] = 2
status = True
pointer = 0
while status:
    intcode,pointer,status = execute_opcode(intcode, pointer)

print(intcode[0])
