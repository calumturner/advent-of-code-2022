with open("input.txt") as f:
    lines = f.read().splitlines()

instructions = [(l.split(' ')[0], int(l.split(' ')[1])) for l in lines]

tail_has_visited = {(0, 0)}
head_position = (0, 0)
tail_position = (0, 0)


def move_head(direction, head_position):
    if direction == 'U':
        return head_position[0], head_position[1] + 1
    if direction == 'D':
        return head_position[0], head_position[1] - 1
    if direction == 'R':
        return head_position[0] + 1, head_position[1]
    if direction == 'L':
        return head_position[0] - 1, head_position[1]


def update_tail(tail_position, head_position, i):
    if tail_position == head_position:
        return tail_position

    # movement = (0, 0)
    # if abs(tail_position[0] - head_position[0]) > 1:
    #     if tail_position[0] == head_position[0] - 2:
    #         # Too far Right
    #         movement = (movement[0]+1, movement[1])
    #
    #     if tail_position[0] == head_position[0] + 2:
    #         # Too far Left
    #         movement = (movement[0] - 1, movement[1])
    # if abs(tail_position[1] - head_position[1]) > 1:
    #     if tail_position[1] == head_position[1] - 2:
    #         # Too far Up
    #         movement = (movement[0], movement[1] + 1)
    #
    #     if tail_position[1] == head_position[1] + 2:
    #         # Too far Down
    #         movement = (movement[0], movement[1] - 1)
    # return tail_position[0] + movement[0], tail_position[1] + movement[1]

    x_diff = abs(tail_position[0] - head_position[0])
    y_diff = abs(tail_position[1] - head_position[1])

    if x_diff > 1 or y_diff > 1:
        x_mov = 0
        y_mov = 0
        if x_diff > 0:
            if (tail_position[0] - head_position[0]) < 0:
                # Too far Right
                x_mov = 1
            else:
                # Too far Left
                x_mov = -1
        if y_diff > 0:
            if (tail_position[1] - head_position[1]) > 0:
                # Too far Down
                y_mov = -1
            else:
                # Too far Up
                y_mov = 1
        return tail_position[0] + x_mov, tail_position[1] + y_mov

    return tail_position




for (direction, steps) in instructions:
    for i in range(steps):
        head_position = move_head(direction, head_position)
        tail_position = update_tail(tail_position, head_position, i)
        tail_has_visited.add(tail_position)

# print(len(tail_has_visited))

head_position = (0, 0)
knotted_tail_visited = {(0, 0)}
knots_positions = [(0, 0) for _ in range(0, 9)]
for (direction, steps) in instructions:
    for _ in range(steps):
        head_position = move_head(direction, head_position)
        knots_positions[0] = update_tail(knots_positions[0], head_position, 0)
        for i in range(1, 9):
            knots_positions[i] = update_tail(knots_positions[i], knots_positions[i - 1], i)
            if i == 8:
                print(knots_positions[i])
                knotted_tail_visited.add(knots_positions[i])

    # a = 30
    # half_a = int(a/2)
    # state = [['.' for _ in range(a)] for _ in range(a)]
    # state[-head_position[1]+half_a][head_position[0]+ half_a] = 'H'
    # for i in range(len(knots_positions)):
    #     x, y = knots_positions[i]
    #     state[-y+half_a][x+half_a] = str(i + 1)
    # for s in state:
    #     print(''.join(s))


print(len(knotted_tail_visited))