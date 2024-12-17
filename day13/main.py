import math
filename = "input.txt"

file = open(filename, "r")

class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

machines = []

for i,line in enumerate(file):
    index = i // 4
    if i % 4 == 0 or (i - 1) % 4 == 0:
        text = line.split('+')
        t1 = text[1]
        t2 = text[2]
        t1 = int(t1.split(',')[0])
        t2 = int(t2.split("\n")[0])
        if i % 4 == 0:
            machines.append(Machine((t1,t2), None, None))
        else:
            machines[index].b = (t1,t2)
    if i % 2 == 0 and i % 4 != 0:
        text = line.split('=')
        t1 = text[1]
        t2 = text[2]
        t1 = int(t1.split(',')[0])
        t2 = int(t2.split("\n")[0])
        machines[index].prize = (t1, t2)

def cost(a, b):
    return a*3 + b

# part 1

total_cost = 0
for m in machines:
    target_x, target_y = m.prize
    a_x, a_y = m.a
    b_x, b_y = m.b
    max_a = math.ceil(max([target_x / a_x, target_y / a_y]))
    max_b = math.ceil(max([target_x / b_x, target_y / b_y]))
    min_cost = None
    min_a = None
    min_b = None
    for a in range(0, max_a+1):
        for b in range(max_b, -1, -1):
            if a * a_x + b * b_x == target_x and a * a_y + b * b_y == target_y:
                c = cost(a, b)
                if min_cost is None or c < min_cost:
                    min_a = a
                    min_b = b
                    min_cost = c
    if min_cost:
        total_cost += min_cost
print(total_cost)

# part 2
# should solve a simultaneous equation
# x_a * a + x_b * b = x_total
# y_a * a + y_b * b = y_total
#
# e.g 
# 94a + 34b = 10000000008400
# 22a + 67b = 10000000005400
