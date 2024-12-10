filename = "input.txt"

file = open(filename, "r")

map = []
for line in file:
    map.append([int(m) for m in line if m != "\n"])

# trail heads represented by (height, x, y)
trails = []
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            trails.append([(x,y)])

num_trails = 0
done = False
while not done:
    done = True
    for trail in trails:
        x, y = trail[-1]
        height = len(trail) - 1
        if height != 9:
            trails.remove(trail)
        if y > 0 and map[y-1][x] == height + 1:
            done = False
            new_trail = [t for t in trail]
            new_trail.append((x, y-1))
            trails.append(new_trail)

        if y < len(map) - 1 and map[y+1][x] == height + 1:
            done = False
            new_trail = [t for t in trail]
            new_trail.append((x, y+1))
            trails.append(new_trail)

        if x > 0 and map[y][x-1] == height + 1:
            done = False
            new_trail = [t for t in trail]
            new_trail.append((x-1, y))
            trails.append(new_trail)

        if x < len(map[0]) - 1 and map[y][x+1] == height + 1:
            done = False
            new_trail = [t for t in trail]
            new_trail.append((x+1, y))
            trails.append(new_trail)

def print_trail(trail):
    map_string = ""
    for y in range(len(map)):
        for x in range(len(map[0])):
            in_trail = False
            for t in trail:
                if (x,y) in t:
                    in_trail = True
            if in_trail:
                map_string+= str(map[y][x])
            else: map_string += "."
        map_string += "\n"
    print(map_string)

trailheads = {}
for t in trails:
    if str(t[0]) in trailheads.keys():
        trailheads[str(t[0])].append(t)
    else:
        trailheads[str(t[0])] = [t]

pt1_sum = 0
pt2_sum = 0
for t in trailheads.keys():
    pt2_sum += len(trailheads[t])
    # remove dupes
    tails = []
    for l in trailheads[t]:
        if l[-1] not in tails:
            tails.append(l[-1])
        else:
            trailheads[t] = [i for i in trailheads[t] if i != l]
    pt1_sum += len(trailheads[t])

print(pt1_sum)
print(pt2_sum)
