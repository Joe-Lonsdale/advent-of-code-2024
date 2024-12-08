filename = "input.txt"

file = open(filename, "r")

grid = []
for line in file:
    grid.append([g for g in line if g != "\n"])

nodes = {}
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == ".":
            continue
        if grid[y][x] not in nodes.keys():
            nodes[grid[y][x]] = [(x,y)]
        else:
            nodes[grid[y][x]].append((x,y))

antinode_grid = [['.' for j in range(len(grid[0]))] for i in range(len(grid))]

for node in nodes.keys():
    for i in nodes[node]:
        for j in nodes[node]:
            if i == j: continue
            antinode_grid[i[1]][i[0]] = '#'
            antinode_grid[j[1]][j[0]] = '#'
            x_dist = j[0] - i[0]
            y_dist = j[1] - i[1]
            new_y = i[1] - y_dist
            new_x = i[0] - x_dist
            while new_y >= 0 and new_y < len(antinode_grid) and new_x >= 0 and new_x < len(antinode_grid[0]):
                antinode_grid[new_y][new_x] = '#'
                new_y -= y_dist
                new_x -= x_dist

            new_y = j[1] + y_dist
            new_x = j[0] + x_dist
            while new_y >= 0 and new_y < len(antinode_grid) and new_x >= 0 and new_x < len(antinode_grid[0]):
                antinode_grid[new_y][new_x] = '#'
                new_y += y_dist
                new_x += x_dist

num_antinodes = sum([y.count('#') for y in antinode_grid])

print(antinode_grid)
print(num_antinodes)