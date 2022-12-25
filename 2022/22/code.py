import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

instructions = lines[-1]
map =lines[:len(lines)-2]
# print(instructions,map)
i=0
j=1
r=0
c=0
def move(r,c,steps,turn,direction):
    if map[r][c] == "#":
        print("crash", r, c, map[r], direction, steps)
        
    else:
        for i in range(steps):
            if r < 0 or c < 0 or r >= len(map) or c >= len(map[r]):
                print("row end")
                if direction == "D":
                    r = 0
                    while map[r][c] != "." or map[r][c] != "#":
                        r = r+1
                if direction == "U":
                    r = len(map)-1
                    while map[r][c] != "." or map[r][c] != "#":
                        r = r-1
                if direction == "L":
                    c = len(map[r])-1
                    while map[r][c] != "." or map[r][c] != "#":
                        c = c-1
                if direction == "R":
                    c = 0
                    while map[r][c] != "." or map[r][c] != "#":
                        c = c+1
            if map[r][c]=="#":
                print("crash", r, c, map[r], direction,i)
                break
            elif map[r][c] == ".":
                if direction == "D":
                    r = r+1
                elif direction == "U":
                    r=r-1
                elif direction == "L":
                    c=c-1
                elif direction == "R":
                    c = c+1
            else:
                print("row end")
                if direction == "D":
                    r=0
                    while map[r][c] != "." or map[r][c] != "#":
                        r = r+1
                if direction == "U":
                    r = len(map)-1
                    while map[r][c] != "." or map[r][c] != "#":
                        r = r-1
                if direction == "L":
                    c=len(map[r])-1
                    while map[r][c] != "." or map[r][c] != "#":
                        c = c-1
                if direction == "R":
                    c = 0
                    while map[r][c] != "." or map[r][c] != "#":
                        c = c+1

                break
    if turn == "L":
        if direction == "D":
            direction = "R"
        elif direction == "U":
            direction = "L"
        elif direction == "L":
            direction = "D"
        elif direction == "R":
            direction = "U"
        # c = c-1
    elif turn == "R":
        if direction == "D":
            direction = "L"
        elif direction == "U":
            direction = "R"
        elif direction == "L":
            direction = "U"
        elif direction == "R":
            direction = "D"
            # r=r+1
        # c=c+1
    return r,c,direction    


direction="R"
while j<len(instructions):
     if instructions[j] =="L":
         print(int(instructions[i:j]), instructions[j])
         
         r, c, direction = move(
             r, c, int(instructions[i:j]), instructions[j], direction)
         i = j+1
        #  break
     if instructions[j] == "R":
        #  print(instructions[i:j])
         print(int(instructions[i:j]), instructions[j])
         r, c, direction = move(
             r, c, int(instructions[i:j]), instructions[j], direction)
         i = j+1
        #  break
    #  print( r, c, direction)
     j=j+1
print(r,c,direction)