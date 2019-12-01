#!/usr/bin/env python

input = open("input", "r")
sum = 0
for val in input:
     while int(val) > 0:
        val = int((int(val) / 3) - 2)
        if val > 0:
            sum += val

print(sum)
