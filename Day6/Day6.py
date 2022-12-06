
with open("input.txt") as f:
    lines = f.read().splitlines()


def part1(data):
    index = 4
    seq = data[:index]
    while index < len(data):
        if len(set(seq)) == 4:
            print(f"Marker found: {index}")
            break
        seq = seq[1:]
        seq.append(data[index])
        index += 1


def part2(data):
    index = 14
    seq = data[:index]
    while index < len(data):
        if len(set(seq)) == 14:
            print(f"Marker found: {index}")
            break
        seq = seq[1:]
        seq.append(data[index])
        index += 1

for data_str in lines:
    data = list(data_str)

    part2(data)


