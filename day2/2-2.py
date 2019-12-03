#!/usr/bin/env python

import sys

def execute_opcode(intcode,pointer):
    if intcode[pointer] == 1:
        noun = int(intcode[intcode[pointer + 1]])
        verb = int(intcode[intcode[pointer + 2]])
        value = noun + verb
        intcode[intcode[pointer + 3]] = noun + verb
        status = True
    elif intcode[pointer] == 2:
        noun = int(intcode[intcode[pointer + 1]])
        verb = int(intcode[intcode[pointer + 2]])
        value = noun * verb
        intcode[intcode[pointer + 3]] = value
        status = True
    else:
        status = False
    pointer = pointer + 4
    return intcode,pointer,status

def check_pair(noun, verb, value):
    if value == 19690720:
        print(f"{100 * noun + verb}")
        sys.exit()



noun = 0
verb = 0
last_verb = True

while True:
    input = open("input", "r")
    intcode = input.read().split(",")
    intcode = [ int(x) for x in intcode ]
    intcode[1] = noun
    intcode[2] = verb
    status = True
    pointer = 0
    while status:
        intcode,pointer,status = execute_opcode(intcode, pointer)
    check_pair(noun, verb, intcode[0])
    if noun == 99:
        verb += 1
        noun = 0
    else:
        noun += 1
        


print(intcode[0])
