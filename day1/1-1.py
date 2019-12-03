#!/usr/bin/env python

input = open("input", "r")
sum = 0
for val in input:
     sum += int((int(val) / 3) - 2)
     

print(sum)
