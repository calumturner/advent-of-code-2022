

with open("input.txt") as f:
    lines = f.read().splitlines()

split_index = lines.index('')
start_state = lines[:split_index]
instructions = []
for instruction in lines[split_index+1:]:
    split_instruction = instruction.split(' ')
    instructions.append((int(split_instruction[1]), int(split_instruction[3])-1, int(split_instruction[5])-1))


number_of_stacks = int(start_state[-1][-1])
reversed_stack = start_state[:-1]
reversed_stack.reverse()
stacks = [[] for _ in range(number_of_stacks)]
for line in reversed_stack:
    for stack_index in range(number_of_stacks):
        if len(line) < stack_index*4+1:
            continue
        value = line[stack_index*4+1]
        if value != ' ':
            stacks[stack_index].append(value)


def part1(instructions, stacks):
    for instruction in instructions:
        for _ in range(instruction[0]):
            value = stacks[instruction[1]].pop()
            stacks[instruction[2]].append(value)



def part2(instructions, stacks):
    for instruction in instructions:
        stacks[instruction[2]].extend(stacks[instruction[1]][-instruction[0]:])
        for _ in range(instruction[0]):
            stacks[instruction[1]].pop()


part2(instructions, stacks)
top_values = []
for stack in stacks:
    if len(stack) > 0:
        top_values.append(stack.pop())
print(''.join(top_values))
print()

