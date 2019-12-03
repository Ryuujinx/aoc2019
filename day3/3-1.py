#!/usr/bin/env python

input = open("input", "r")
instructions_wire1,instructions_wire2 = input.readlines()


wire1 = {"0,0":0}
wire2 = {"0,0":0}
intersections = []
current_x = 0
current_y = 0
for direction in instructions_wire1.split(","):
    cardinal = direction[0]
    distance = direction[1:]
    if cardinal == "L":
        for node in range(int(current_x), int(current_x) - int(distance), -1):
            if f"{int(node)},{current_y}" not in wire1:
                wire1[f"{int(node)},{current_y}"] = 1
            current_x = int(current_x) - 1
    elif cardinal == "R":
        for node in range(int(current_x), int(current_x) + int(distance), 1):
            if f"{int(node)},{current_y}" not in wire1:
                wire1[f"{int(node)},{current_y}"] = 1
            current_x = int(current_x) + 1
    elif cardinal == "U":
        for node in range(int(current_y), int(current_y) + int(distance), 1):
            if f"{current_x},{int(node)}" not in wire1:
                wire1[f"{current_x},{int(node)}"] = 1
            current_y = int(current_y) + 1
    elif cardinal == "D":
        for node in range(int(current_y), int(current_y) - int(distance), -1):
            if f"{current_x},{int(node)}" not in wire1:
                wire1[f"{current_x},{int(node)}"] = 1
            current_y = int(current_y) - 1

current_x = 0
current_y = 0
for direction in instructions_wire2.split(","):
    cardinal = direction[0]
    distance = direction[1:]
    if cardinal == "L":
        for node in range(int(current_x), int(current_x) - int(distance), -1):
            if f"{int(node)},{current_y}" not in wire2:
                wire2[f"{int(node)},{current_y}"] = 1
                if f"{int(node)},{current_y}" in wire1:
                    if f"{int(node)},{current_y}" not in intersections:
                        intersections.append(f"{int(node)},{current_y}")
            current_x = int(current_x) - 1
    elif cardinal == "R":
        for node in range(int(current_x), int(current_x) + int(distance), 1):
            if f"{int(node)},{current_y}" not in wire2:
                wire2[f"{int(node)},{current_y}"] = 1
                if f"{int(node)},{current_y}" in wire1:
                    if f"{int(node)},{current_y}" not in intersections:
                        intersections.append(f"{int(node)},{current_y}")
            current_x = int(current_x) + 1
    elif cardinal == "U":
        for node in range(int(current_y), int(current_y) + int(distance), 1):
            if f"{current_x},{int(node)}" not in wire2:
                wire2[f"{current_x},{int(node)}"] = 1
                if f"{current_x},{int(node)}" in wire1:
                    if f"{current_x},{int(node)}" not in intersections:
                        intersections.append(f"{current_x},{int(node)}")
            current_y = int(current_y) + 1
    elif cardinal == "D":
        for node in range(int(current_y), int(current_y) - int(distance), -1):
            if f"{current_x},{int(node)}" not in wire2:
                wire2[f"{current_x},{int(node)}"] = 1
                if f"{current_x},{int(node)}" in wire1:
                    if f"{current_x},{int(node)}" not in intersections:
                        intersections.append(f"{current_x},{int(node)}")
            current_y = int(current_y) - 1


smol_boi = 50000
for xy_pair in intersections:
    x,y = xy_pair.split(",")
    if abs(int(x)) + abs(int(y)) < smol_boi:
        smol_boi = abs(int(x)) + abs(int(y))
    

print(smol_boi)