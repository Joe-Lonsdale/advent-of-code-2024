filename = "input.txt"

file = open(filename, "r")
seen_stones = {}

class Stone:
    def __init__(self, label, origin):
        self.label = label
        self.seen = 0
        self.produces = []
        self.origins = [origin]
        self.origins = [s for s in self.origins if s is not None]
        self.length_after_n = []
                
    def process(self):
        if len(self.produces) != 0: return
        if int(self.label) == 0:
            if '1' not in seen_stones:
                seen_stones['1'] = Stone('1', self)
            self.produces.append(seen_stones['1'])

        elif len(self.label) % 2 == 0:
            first_label = str(int(self.label[:int(len(self.label)/2)]))
            second_label = str(int(self.label[int(len(self.label)/2):]))
            for label in [first_label, second_label]:
                if label not in seen_stones:
                    seen_stones[label] = Stone(label, self)
                self.produces.append(seen_stones[label])
        else:
            label = str(int(self.label) * 2024)
            if label not in seen_stones:
                seen_stones[label] = Stone(label, self)
            self.produces.append(seen_stones[label])
    

    def __str__(self):
        return f"[{self.label}, {self.seen}, {[s.label for s in self.produces]}]"


stones = []
for line in file:
    stones = line.split(" ")
    stones = [Stone(s, None) for s in stones]
    for s in stones:
        s.process()

num_iters = 75
curr_length = len(stones)

for i in range(num_iters):
    print(f"{i}/{num_iters}")
    new_stones = []
    for stone in stones:
        results = None
        if stone.seen > 0:
            results = stone.produces
        else:
            stone.process()
            results = stone.produces
            stone.seen += 1
        new_stones.extend(results)
    stones = new_stones
    
# print("---------------------")
# for s in stones:
#     print(s)
# print("---------------------")


print(len(stones))
