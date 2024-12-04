import regex as re
filename = "input.txt"

file = open(filename, "r")
lines = file.readlines()
lines_concatenated = ""
for line in lines:
    lines_concatenated += line

muls = re.findall("mul\(\d*,\d*\)", lines_concatenated)

def do_mul(input):
    xs = input.split(",")
    m1 = xs[0].replace("mul(","")
    m2 = xs[1].replace(")","")
    return int(m1) * int(m2)

total = 0
for mul in muls:
    total += do_mul(mul)

#part 1
print(total)

indexes_of_do = []
indexes_of_dont = []

ls = lines_concatenated
last_found = 0
for x in range(ls.count("do()")):
    indexes_of_do.append(ls.find("do()", last_found))
    last_found = indexes_of_do[-1] + 1
last_found = 0
for x in range(ls.count("don't()")):
    indexes_of_dont.append(ls.find("don't()", last_found))
    last_found = indexes_of_dont[-1] + 1

def find_enabled_periods(dos, donts):
    enabled = []
    enabled.append((0,donts[0]))
    curr = donts[0]
    for do in dos:
        if curr > do: continue
        enabled.append((do, min([d for d in donts if d > do])))
        curr = enabled[-1][1]
    return enabled

enabled = find_enabled_periods(indexes_of_do, indexes_of_dont)
enabled_lines = ""
for e in enabled:
    enabled_lines += lines_concatenated[e[0]:e[1]]

muls = re.findall("mul\(\d*,\d*\)", enabled_lines)

total = 0
for mul in muls:
    total += do_mul(mul)

#part 2
print(total)