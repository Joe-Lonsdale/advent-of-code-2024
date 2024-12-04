filename = "input.txt"

file = open(filename, "r")

ws = []
for line in file:
    ws.append([l for l in line if l != '\n'])

#part 1
total = 0
for y in range(len(ws)):
    for x in range(len(ws[y])):
        if ws[y][x] != 'X': continue
        if x > 2:
            # check left
            if ws[y][x-1] == 'M' and ws[y][x-2] == 'A' and ws[y][x-3] == 'S':
                total += 1
            # check up left
            if y > 2:
                if ws[y-1][x-1] == 'M' and ws[y-2][x-2] == 'A' and ws[y-3][x-3] == 'S':
                    total += 1
            # check down left
            if y < len(ws) - 3:
                if ws[y+1][x-1] == 'M' and ws[y+2][x-2] == 'A' and ws[y+3][x-3] == 'S':
                    total += 1
        if x < len(ws[y]) - 3:
            # check right
            if ws[y][x+1] == 'M' and ws[y][x+2] == 'A' and ws[y][x+3] == 'S':
                total += 1
            # check up right
            if y > 2:
                if ws[y-1][x+1] == 'M' and ws[y-2][x+2] == 'A' and ws[y-3][x+3] == 'S':
                    total += 1
            # check down right
            if y < len(ws) - 3:
                if ws[y+1][x+1] == 'M' and ws[y+2][x+2] == 'A' and ws[y+3][x+3] == 'S':
                    total += 1
        # check up 
        if y > 2:
            if ws[y-1][x] == 'M' and ws[y-2][x] == 'A' and ws[y-3][x] == 'S':
                total += 1
        # check down 
        if y < len(ws) - 3:
            if ws[y+1][x] == 'M' and ws[y+2][x] == 'A' and ws[y+3][x] == 'S':
                total += 1

print(total)

#part2
total = 0
for y in range(len(ws)):
    for x in range(len(ws[y])):
        if y == 0 or y == len(ws) - 1: continue
        if x == 0 or x == len(ws[y]) - 1: continue
        if ws[y][x] != 'A': continue
        if ws[y-1][x-1] == 'M' and ws[y-1][x+1] == 'M' and ws[y+1][x+1] == 'S' and ws[y+1][x-1] == 'S':
            total += 1
        if ws[y-1][x-1] == 'S' and ws[y-1][x+1] == 'M' and ws[y+1][x+1] == 'M' and ws[y+1][x-1] == 'S':
            total += 1
        if ws[y-1][x-1] == 'S' and ws[y-1][x+1] == 'S' and ws[y+1][x+1] == 'M' and ws[y+1][x-1] == 'M':
            total += 1
        if ws[y-1][x-1] == 'M' and ws[y-1][x+1] == 'S' and ws[y+1][x+1] == 'S' and ws[y+1][x-1] == 'M':
            total += 1
print(total)
