filename = "input.txt"

file = open(filename, "r")

instructions = {}
updates = []

for line in file:
    if "|" in line:
        # instruction
        s = line.split("|")
        first = s[0]
        second = int(s[1])
        if first in instructions.keys():
            instructions[first].append(second)
        else:
            instructions[first] = [second]
    else:
        if "," in line:
            # update
            nums = line.split(",")
            updates.append([int(x) for x in nums])

def is_ordered(update):
    for later in range(len(update)-1, 0, -1):
        for earlier in range(later-1, -1, -1):
            if str(update[later]) in instructions.keys() and update[earlier] in instructions[str(update[later])]:
                return False
    return True

def find_incorrect_values(update):
    flagged = []
    for later in range(len(update)-1, 0, -1):
        for earlier in range(later-1, -1, -1):
            if str(update[later]) in instructions.keys() and update[earlier] in instructions[str(update[later])]:
                flagged.append(update[later])
    return flagged

valid_updates = []
invalid_updates = []
for update in updates:
    if is_ordered(update):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

# part 1
sum = 0
for update in valid_updates:
    sum += update[int(len(update) / 2)]
print(sum)

# part 2

def reorder(update):
    # check if in order.
    # if true then finish.
    # if false, flag all incorrect values.
    # for latest value, shift left 1 until that isn't flagged any more.
    # do this until ordered.
    flagged = find_incorrect_values(update)
    if flagged == []: return update
    reordered = [u for u in update]
    while len(flagged) != 0:
        index = reordered.index(flagged[-1])
        temp = reordered[index]
        reordered[index] = reordered[index-1]
        reordered[index-1] = temp
        flagged = find_incorrect_values(reordered)

    return reordered

reordered = []
for invalid in invalid_updates:
    reordered.append(reorder(invalid))

sum = 0
for update in reordered:
    sum += update[int(len(update) / 2)]
print(sum)