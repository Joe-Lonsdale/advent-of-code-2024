import time
import os
filename = "input.txt"

file = open(filename, "r")

map = []
for line in file:
    map.append([l for l in line if l != "\n"])

fresh_map = [[l for l in x] for x in map]
pos_x = -1
pos_y = -1
facing = "UP"
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            pos_x = x
            pos_y = y

def print_map():
    s = ""
    for y in range(len(map)):
        for x in range(len(map[y])):
            s += map[y][x]
        s+="\n"
    print(s)

while pos_x > 0 and pos_x < len(map[0]) and pos_y > 0 and pos_y < len(map):
    # time.sleep(0.1)
    # os.system('cls')
    map[pos_y][pos_x] = "X"
    print(pos_x, pos_y)
    if facing == "UP":
        if pos_y == 0:
            pos_y -= 1
        elif map[pos_y - 1][pos_x] == '#':
            facing = "RIGHT"
        else: pos_y -= 1
    elif facing == "RIGHT":
        if pos_x == len(map) - 1:
            pos_x += 1
        elif map[pos_y][pos_x + 1] == '#':
            facing = "DOWN"
        else: pos_x += 1
    elif facing == "DOWN":
        if pos_y == len(map) - 1:
            pos_y += 1
        elif map[pos_y + 1][pos_x] == '#':
            facing = "LEFT"
        else: pos_y += 1
    else:
        if pos_x == 0:
            pos_x -= 1
        elif map[pos_y][pos_x - 1] == '#':
            facing = "UP"
        else: pos_x -= 1
    # print_map()
count = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "X":
            count += 1
print_map()
print(count)

# part 2:
'''
idea:
we only care about the points at which the path overlaps after hitting exactly 3 obstacles.
considering these points should give us the points at which a loop can be made.

while travelling the line, put 1 at all the positions on the path until you hit a block.
then, turn all 1s into 2s, 2s into 3s, 3s into 4s, and 4s into Xs.
if the current square you're on has 4 in it, you can place a obstacle in the square in front of you to make a loop.
'''
map = fresh_map
pos_x = -1
pos_y = -1
facing = "UP"
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            pos_x = x
            pos_y = y
            map[y][x] = '1'

def increase():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '4':
                map[y][x] = 'X'
            if map[y][x] == '3':
                map[y][x] = '4'
            if map[y][x] == '2':
                map[y][x] = '3'
            if map[y][x] == '1':
                map[y][x] = '2'

def get_all_expanded_loops(x, y, facing):
    possible_loops += 1
    if facing == "UP":
        
    elif facing == "RIGHT":

    elif facing == "DOWN":

    else:


possible_loops = 0
while pos_x > 0 and pos_x < len(map[0]) and pos_y > 0 and pos_y < len(map):
    if map[pos_y][pos_x] == "4":
        get_all_expanded_loops(pos_x, pos_y, facing)
    map[pos_y][pos_x] = "1"
    print(pos_x, pos_y)
    if facing == "UP":
        if pos_y == 0:
            pos_y -= 1
        elif map[pos_y - 1][pos_x] == '#':
            increase()
            facing = "RIGHT"
        else: pos_y -= 1
    elif facing == "RIGHT":
        if pos_x == len(map) - 1:
            pos_x += 1
        elif map[pos_y][pos_x + 1] == '#':
            increase()
            facing = "DOWN"
        else: pos_x += 1
    elif facing == "DOWN":
        if pos_y == len(map) - 1:
            pos_y += 1
        elif map[pos_y + 1][pos_x] == '#':
            increase()
            facing = "LEFT"
        else: pos_y += 1
    else:
        if pos_x == 0:
            pos_x -= 1
        elif map[pos_y][pos_x - 1] == '#':
            increase()
            facing = "UP"
        else: pos_x -= 1

print(map)
print(possible_loops)