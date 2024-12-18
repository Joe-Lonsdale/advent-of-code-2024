import random
filename = "input.txt"

file = open(filename, "r")

initial_registers = {}
target_program = []
ip = 0
jumped = False

for line in file:
    if line.startswith("Register"):
        l = line.split(":")
        reg = l[0][-1]
        val = int(l[1][1:])
        initial_registers[reg] = val
    if line.startswith("Program"):
        l = line.split(":")
        target_program = [int(r) for r in l[1][1:].split(',')]

def get_combo(operand, registers):
    if operand in [4,5,6]:
        return registers[list(registers.keys())[operand - 4]]
    return operand

def adv(operand, registers):
    operand = get_combo(operand, registers)
    registers['A'] = int(registers['A'] / (2 ** operand))

def xor(a, b):
    return a ^ b

def bxl(operand, registers):
    registers['B'] = xor(registers['B'], operand)

def bst(operand, registers):
    operand = get_combo(operand, registers)
    registers['B'] = operand % 8

def jnz(operand, registers):
    if registers['A'] == 0:
        return None
    return operand

def bxc(operand, registers):
    registers['B'] = xor(registers['B'], registers['C'])

def out(operand, registers):
    global output
    operand = get_combo(operand, registers)
    return operand % 8

def bdv(operand, registers):
    operand = get_combo(operand, registers)
    registers['B'] = int(registers['A'] / (2 ** operand))

def cdv(operand, registers):
    operand = get_combo(operand, registers)
    registers['C'] = int(registers['A'] / (2 ** operand))

def run_program(program=target_program, registers={x:initial_registers[x] for x in initial_registers.keys()}):
    ip = 0
    output = []
    while ip < len(program):
        jumped = False
        opcode = program[ip]
        operand = program[ip+1]
        if opcode == 0:
            adv(operand, registers)
        elif opcode == 1:
            bxl(operand, registers)
        elif opcode == 2:
            bst(operand, registers)
        elif opcode == 3:
            to_jump = jnz(operand, registers)
            if to_jump is not None:
                ip = to_jump
                jumped = True
        elif opcode == 4:
            bxc(operand, registers)
        elif opcode == 5:
            output.append(out(operand, registers))
        elif opcode == 6:
            bdv(operand, registers)
        elif opcode == 7:
            cdv(operand, registers)
        if not jumped:
            ip += 2
            jumped = False
    return output
        

#pt 1
output = run_program()
os = ""
for o in output:
    os += f"{o},"
print(f"part 1: {os[:-1]}")

#pt 2

class Individual:
    def __init__(self, bits):
        self.bits = bits
        self.output = None
        self.fitness = 0

    def calculate_fitness(self):
        if self.output is None:
            self.fitness = 0
            return
        total = 1000 ** abs(len(self.output) - len(target_program))
        i = len(target_program)
        for pair in zip(self.output, target_program):
            total += 2 ** (i * abs(pair[0] - pair[1]))
            i -= 1 if i > 0 else 0
        total += float(f"0.{int("".join(str(x) for x in self.bits), 2)}")
        self.fitness = total

    def mutate(self, mutation_rate):
        for i in range(len(self.bits)):
            if random.random() < mutation_rate:
                self.bits[i] = int(not self.bits[i])
    
    def __str__(self):
        return f"Register A: {int("".join(str(x) for x in self.bits), 2)}, Output: {self.output}"

def genetic_algorithm(num_iters, pop_size, mutation_rate):
    # initialise population with random bits
    population = []
    overall_best = None
    for p in range(pop_size):
        individual_num = random.randint(2**45, 2**48-1)
        individual = Individual([int(digit) for digit in bin(individual_num)[2:]])
        population.append(individual)
        registers={x:initial_registers[x] for x in initial_registers.keys()}
        registers['A'] = int("".join(str(x) for x in individual.bits), 2)
        individual.output = run_program(registers=registers)
        individual.calculate_fitness()
    
    def tournament(k, population):
        participants = random.sample(population, k)
        participants.sort(key=lambda x: x.fitness)
        return participants[0]

    def crossover(parent_1, parent_2):
        new_bits = []
        for pair in zip(parent_1.bits, parent_2.bits):
            new_bits.append(pair[random.randint(0,1)])
        return Individual(new_bits)    
    
    for iteration in range(1, num_iters+1):
        print(f"------------------------\nIteration {iteration} / {num_iters}\n")
        for individual in population:
            registers={x:initial_registers[x] for x in initial_registers.keys()}
            registers['A'] = int("".join(str(x) for x in individual.bits), 2)
            individual.output = run_program(registers=registers)
            individual.calculate_fitness()
        # selection (tournament, k = 15) and crossover (uniform)
        elite_num = 25
        sorted_pop = sorted(population, key=lambda x: x.fitness)
        new_population = [i for i in sorted_pop][:elite_num]
        for p in range(pop_size - elite_num):
            parent_1 = tournament(15,sorted_pop[:len(population) // 2])
            parent_2 = tournament(15,sorted_pop[:len(population) // 2])
            new_individual = crossover(parent_1,parent_2)
            new_individual.mutate(mutation_rate)
            new_population.append(new_individual)
        # mutation
        for individual in new_population:
            registers={x:initial_registers[x] for x in initial_registers.keys()}
            registers['A'] = int("".join(str(x) for x in individual.bits), 2)
            individual.output = run_program(registers=registers)
            individual.calculate_fitness()

        avg_fitness = sum([i.fitness for i in new_population]) / len(new_population)
        best_individual = sorted(new_population, key=lambda x: x.fitness)[0]
        if overall_best is None or best_individual.fitness < overall_best.fitness:
            overall_best = Individual([b for b in best_individual.bits])
            overall_best.fitness = best_individual.fitness
            overall_best.output = best_individual.output
        print(f"Average fitness: {avg_fitness}\nBest fitness: {best_individual.fitness}\nBest individual: {best_individual}\nOverall best: {overall_best}")
        population = new_population

genetic_algorithm(10000, 10000, 0.1)

# bitfield = [int(digit) for digit in bin(265652340537354)[2:]]
# for i in range(len(bitfield)):
#     modified_bitfield = [b for b in bitfield]
#     modified_bitfield[i] = int(not modified_bitfield[i])
#     registers={x:initial_registers[x] for x in initial_registers.keys()}
#     registers['A'] = registers['A'] = int("".join(str(x) for x in modified_bitfield), 2)
#     output = run_program(registers=registers)
#     if output == target_program:
#         os = ""
#         for o in output:
#             os += f"{o},"
#         print(f"{i}: {os[:-1]}")