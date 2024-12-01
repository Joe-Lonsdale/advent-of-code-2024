filename = "input.txt"

file = open(filename, "r")

list1 = []
list2 = []
for line in file:
    vals = line.split('   ')
    list1.append(int(vals[0]))
    list2.append(int(vals[1]))

list1.sort()
list2.sort()

#part 1
diffs = 0
for i in range(len(list1)):
    diffs += abs(list1[i] - list2[i]) 

#print(diffs)

#part2
sim_score = 0
for i in range(len(list1)):
    sim_score += list2.count(list1[i]) * list1[i]

print(sim_score)