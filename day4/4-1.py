#!/usr/bin/env python

import re
input="265275-781584"

lowerlimit,upperlimit = input.split("-")

paircount = 0
for value in range(int(lowerlimit), int(upperlimit)):
    str_value = str(value)
    if re.search('(.)\\1', str_value):
        if int(str_value[0]) <= int(str_value[1]) and int(str_value[1]) <= int(str_value[2]) and int(str_value[2]) <= int(str_value[3]) and int(str_value[3]) <= int(str_value[4]) and int(str_value[4]) <= int(str_value[5]):
            paircount += 1

print(paircount)
    