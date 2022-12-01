

with open("input.txt") as f:
    readings = f.read().splitlines()

def part1(readings):
    food_per_elf = []
    elf_index = 0
    for reading in readings:
        if reading == '':
            elf_index += 1
            continue
        if len(food_per_elf) <= elf_index:
            food_per_elf.append([int(reading)])
        else:
            food_per_elf[elf_index].append(int(reading))

    calories_per_elf = [sum(food) for food in food_per_elf]
    max_calories = max(calories_per_elf)
    max_calories_index = calories_per_elf.index(max_calories)
    print(f"Elf {max_calories_index} has the most calories: {max_calories}")


def part2(readings):
    food_per_elf = []
    elf_index = 0
    for reading in readings:
        if reading == '':
            elf_index += 1
            continue
        if len(food_per_elf) <= elf_index:
            food_per_elf.append([int(reading)])
        else:
            food_per_elf[elf_index].append(int(reading))

    calories_per_elf = [sum(food) for food in food_per_elf]
    top_three_calories_per_elf = calories_per_elf.copy()
    top_three_total_calories = 0
    for i in range(0, 3):
        max_calories = max(top_three_calories_per_elf)
        top_three_total_calories += max_calories
        max_calories_index = calories_per_elf.index(max_calories)
        print(f"Elf {max_calories_index} has calories: {max_calories}")
        top_three_calories_per_elf[max_calories_index] = 0
    print(f"Total calories of top 3: {top_three_total_calories}")

part1(readings)
print()
part2(readings)