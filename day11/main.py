import multiprocessing
filename = "input.txt"

file = open(filename, "r")

stones = []
for line in file:
    stones = line.split(" ")

num_iters = 25

def process_stone(stone):
    if int(stone) == 0:
        return '1'
    elif len(stone) % 2 == 0:
        return str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))
    else:
        return str(int(stone) * 2024)

seen_stones = {}
seen_counts = {s:1 for s in stones}
curr_length = len(stones)
for i in range(num_iters):
    print(f"{i}/{num_iters}")
    new_stones = []
    for stone in stones:
        results = None
        if stone in seen_stones.keys():
            results = seen_stones[stone]
        else:
            if int(stone) == 0:
                results = ['1']
            elif len(stone) % 2 == 0:
                results = [str(int(stone[:int(len(stone)/2)])),str(int(stone[int(len(stone)/2):]))]
            else:
                results = [str(int(stone) * 2024)]

            seen_stones[stone] = results
        new_stones.extend(results)

    stones = new_stones

# print(stones)
print(len(stones))
