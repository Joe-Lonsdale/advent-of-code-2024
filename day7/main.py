filename = "input.txt"

file = open(filename, "r")

totals = []
values = []
for line in file:
    l = line.split(': ')
    totals.append(int(l[0]))
    values.append([int(x) for x in l[1].split(' ')])

sum_possible = 0

def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)

for i in range(len(totals)):
    print(i)
    target = totals[i]
    vals = values[i]
    num_perms = 3 ** (len(vals) - 1)
    operators = ['+', '*', '||']
    for j in range(num_perms):
        total = 0
        perm = ternary(j).zfill(len(ternary(num_perms)) - 1)
        for op in range(len(perm)):
            if op == 0:
                if int(perm[op]) == 0:
                    total = vals[0] + vals[1]
                elif int(perm[op]) == 1:
                    total = vals[0] * vals[1]
                else:
                    total = int(str(vals[0]) + str(vals[1]))
            else:
                if int(perm[op]) == 0:
                    total += vals[op+1]
                elif int(perm[op]) == 1:
                    total *= vals[op+1]
                else:
                    total = int(str(total) + str(vals[op+1]))
        if total == target:
            sum_possible += target
            break
print(sum_possible)


