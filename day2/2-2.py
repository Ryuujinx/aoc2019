#!/usr/bin/env python

import sys

def execute_opcode(intcode,pointer):
    if intcode[pointer] == 1:
        noun = int(intcode[intcode[pointer + 1]])
        verb = int(intcode[intcode[pointer + 2]])
        intcode[intcode[pointer + 3]] = noun + verb
        check_pair(noun, verb, intcode[intcode[pointer + 3]])
        status = True
    elif intcode[pointer] == 2:
        noun = int(intcode[intcode[pointer + 1]])
        verb = int(intcode[intcode[pointer + 2]])
        intcode[intcode[pointer + 3]] = noun * verb
        check_pair(noun, verb, intcode[intcode[pointer + 3]])
        status = True
    else:
        status = False
    pointer = pointer + 4
    return intcode,pointer,status

def check_pair(noun, verb, value):
    if value == 19690720:
        print(f"{100 * noun + verb}")
        sys.exit()



input = open("input", "r")
intcode = input.read().split(",")
intcode = [ int(x) for x in intcode ]
intcode[1] = 12
intcode[2] = 2
status = True
pointer = 0
while status:
    intcode,pointer,status = execute_opcode(intcode, pointer)


print(intcode[0])
