#!/usr/bin/env python

input = open("input", "r")
instructions_wire1,instructions_wire2 = input.readlines()


step_data = []
intersections = ['-1078,-548', '-877,-656', '-845,-656', '-361,-656', '525,-543', '468,-615', '-315,-846', '-196,-1028', '271,-1464', '372,-1948', '921,-1763', '921,-1459', '921,-1430', '1296,-1081', '1296,-1459', '1220,-1569', '1146,-1459', '1261,-1081', '1261,-1459', '1261,-1720', '1323,-1748', '372,-1877', '372,-2052']
for xy_pair in intersections:
    current_x = 0
    current_y = 0
    wire1_stepcount = 0
    wire2_stepcount = 0
    x,y = xy_pair.split(",")
    for direction in instructions_wire1.split(","):
        cardinal = direction[0]
        distance = direction[1:]
        atintersection = False
        if cardinal == "L":
            for node in range(int(current_x), int(current_x) - int(distance), -1):
                wire1_stepcount += 1
                current_x = int(current_x) - 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "R":
            for node in range(int(current_x), int(current_x) + int(distance), 1):
                wire1_stepcount += 1
                current_x = int(current_x) + 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "U":
            for node in range(int(current_y), int(current_y) + int(distance), 1):
                wire1_stepcount += 1
                current_y = int(current_y) + 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "D":
            for node in range(int(current_y), int(current_y) - int(distance), -1):
                wire1_stepcount += 1
                current_y = int(current_y) - 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        if atintersection:
            break

    current_x = 0
    current_y = 0
    for direction in instructions_wire2.split(","):
        cardinal = direction[0]
        distance = direction[1:]
        atintersection = False
        if cardinal == "L":
            for node in range(int(current_x), int(current_x) - int(distance), -1):
                current_x = int(current_x) - 1
                wire2_stepcount += 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "R":
            for node in range(int(current_x), int(current_x) + int(distance), 1):
                current_x = int(current_x) + 1
                wire2_stepcount += 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "U":
            for node in range(int(current_y), int(current_y) + int(distance), 1):
                current_y = int(current_y) + 1
                wire2_stepcount += 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        elif cardinal == "D":
            for node in range(int(current_y), int(current_y) - int(distance), -1):
                current_y = int(current_y) - 1
                wire2_stepcount += 1
                if current_x == int(x):
                    if current_y == int(y):
                        atintersection = True
                        break
        if atintersection:
            break

    step_data.append(wire1_stepcount + wire2_stepcount)
        

smol_boi = 5000000
for num in step_data:
    if num < smol_boi:
        smol_boi = num

print(smol_boi)