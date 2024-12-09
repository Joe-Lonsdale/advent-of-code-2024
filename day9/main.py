filename = "input.txt"

file = open(filename, "r")

disk_map = []
for line in file:
    disk_map = [l for l in line if l != '\n']

def get_disk_layout(disk_map):
    file = True
    layout = []
    id = 0
    for char in disk_map:
        if file:
            for _ in range(int(char)):
                layout.append(str(id))
            id += 1
        else:
            for _ in range(int(char)):
                layout.append('.')
        file = not file
    return layout

layout = get_disk_layout(disk_map)

def get_earliest_free_space(disk_layout, known_earliest, length=1):
    for i in range(known_earliest, len(disk_layout)):
        if disk_layout[i] == '.':
            found = True
            for j in range(length):
                if i + j >= len(disk_layout):
                    found = False
                    break
                if disk_layout[i+j] != '.':
                    found = False
                    break
            if found: return i
    return -1

def defragment_disk(disk_layout):
    known_earliest = 0
    for i in range(len(disk_layout)-1, -1, -1):
        print(f'{round(100 * (1 - i / len(disk_layout)), 2)}%')
        if disk_layout[i] == '.':
            continue
        earliest_space = get_earliest_free_space(disk_layout, known_earliest)
        known_earliest = earliest_space
        if earliest_space == -1 or i <= earliest_space:
            continue
        disk_layout[earliest_space] = disk_layout[i]
        disk_layout[i] = '.'
    return disk_layout

def compute_checksum(disk_layout):
    return sum([i * int(disk_layout[i]) for i in range(len(disk_layout)) if disk_layout[i] != '.'])

#defragmented = defragment_disk(layout)
#print(compute_checksum(defragmented))

def defragment_with_blocks(disk_layout):
    known_earliest = 0
    checked_blocks = []
    for i in range(len(disk_layout)-1, -1, -1):
        print(f'{round(100 * (1 - i / len(disk_layout)), 2)}%')
        if disk_layout[i] == '.':
            continue
        block_length = 0
        block_id = disk_layout[i]
        if block_id in checked_blocks:
            continue
        checked_blocks.append(block_id)
        while disk_layout[i] ==  block_id:
            i -= 1
            block_length += 1
        i += 1
        potential_earliest = get_earliest_free_space(disk_layout, known_earliest, block_length)
        # print(block_id)
        # print(block_length)
        # print(potential_earliest)
        # print("\n\n")
        if potential_earliest == -1 or i < potential_earliest:
            continue
        for j in range(block_length):
            disk_layout[potential_earliest + j] = disk_layout[i + j]
            disk_layout[i + j] = '.'
        known_earliest = potential_earliest if potential_earliest < known_earliest else known_earliest
        
    return disk_layout

def print_layout(disk_layout):
    str = ""
    for i in disk_layout:
        str += i
    print(str)

defragmented_with_blocks = defragment_with_blocks(layout)
print_layout(defragmented_with_blocks)
print(compute_checksum(defragmented_with_blocks))