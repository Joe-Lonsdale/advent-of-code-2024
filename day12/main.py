filename = "input.txt"

file = open(filename, "r")

garden = []
for line in file:
    garden.append([l for l in line if l != "\n"])

def is_adjacent(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if abs(x1 - x2) == 1 and y1 == y2:
        return True
    if abs(y1 - y2) == 1 and x1 == x2:
        return True
    return False

def consolidate_plots(plots):
    for plant in plots:
        for plot in plots[plant]:
            for point in plot:
                for other_plot in plots[plant]:
                    consolidated = False
                    if other_plot == plot: continue
                    for other_point in other_plot:
                        if consolidated: continue
                        if is_adjacent(point, other_point):
                            plot.extend(other_plot)
                            plots[plant].remove(other_plot)
                            consolidated = True
    return plots

def get_plots(garden):
    plots = {}
    for y in range(len(garden)):
        for x in range(len(garden[0])):
            plant = garden[y][x]
            if plant not in plots.keys():
                plots[plant] = [[(x,y)]]
            else:
                adjacent = False
                for plot in plots[plant]:
                    for coord in plot:
                        if is_adjacent((x,y), coord) and not adjacent:
                            adjacent = True
                            plot.append((x,y))
                if not adjacent:
                    plots[plant].append([(x,y)])
    plots = consolidate_plots(plots)
    return plots

def count_adjacent(garden, point):
    x1 = point[0]
    y1 = point[1]
    plant = garden[y1][x1]
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if abs(x) == abs(y): continue
            if y1+y not in range(0, len(garden)) or x1+x not in range(0, len(garden[0])): continue
            if garden[y1+y][x1+x] == plant:
                count += 1
    return count

def get_area(plot):
    return len(plot)

def get_perimeter(plot):
    perimeter = 0
    for point in plot:
        perimeter += 4 - count_adjacent(garden, point)
    return perimeter

def get_new_perimeter(plot):
    # first get outer edges (points with < 4 adjacent)
    # then figure out whether each edge is north,east,south,west
    outer = {dir:[] for dir in ['n','e','s','w']}
    for point in plot:
        x = point[0]
        y = point[1]
        if count_adjacent(garden, point) < 4:
            if (x, y-1) not in plot:
                outer['n'].append(point)
            if (x, y+1) not in plot:
                outer['s'].append(point)
            if (x-1, y) not in plot:
                outer['w'].append(point)
            if (x+1, y) not in plot:
                outer['e'].append(point)
    # then we join all adjacent points into lists representing straight edges
    edges = []
    for dir in outer:
        dir_edges = []
        for point in outer[dir]:
            adjacent = False
            for edge in dir_edges:
                for other_point in edge:
                    if is_adjacent(point, other_point):
                        edge.append(point)
                        adjacent = True
            if not adjacent:
                dir_edges.append([point])
        # consolidate edges
        for edge in dir_edges:
            for other_edge in dir_edges:
                consolidated = False
                if edge == other_edge: continue
                for point in edge:
                    if consolidated: continue
                    for other_point in other_edge:
                        if is_adjacent(point, other_point):
                            edge.extend(other_edge)
                            dir_edges.remove(other_edge)
                            consolidated = True
        edges.extend(dir_edges)
    # just return number of edges
    return len(edges)

def print_plot(plot):
    xs = [p[0] for p in plot]
    ys = [p[1] for p in plot]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    output = ""
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in plot:
                output += garden[y][x]
            else:
                output += " "
        output += "\n"
    print(output)


plots = get_plots(garden)

# pt 1

# for p in plots:
#     print("--------------------")
#     print(p)
#     for area in plots[p]:
#         print(f"{area}\nArea: {get_area(area)}\nPerimeter: {get_perimeter(area)}")
#     print("--------------------\n")


# pt 2

for p in plots:
    print("--------------------")
    print(p)
    for area in plots[p]:
        print(f"Area: {get_area(area)}\nPerimeter: {get_new_perimeter(area)}\n")
        print_plot(area)
    print("--------------------\n")

total = 0
for p in plots:
    for area in plots[p]:
        total += get_area(area) * get_perimeter(area)
print(f"Total price: {total}")

total = 0
for p in plots:
    for area in plots[p]:
        total += get_area(area) * get_new_perimeter(area)
print(f"Total price: {total}")
