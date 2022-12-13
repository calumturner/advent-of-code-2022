
with open("input.txt") as f:
    lines = f.read().splitlines()


class Node:
    def __init__(self, parent, x, y, value) -> None:
        self.x = x
        self.y = y
        self.parent = parent
        self.value = value

    def __repr__(self) -> str:
        return f"Node({self.x}, {self.y}, {self.parent}, {self.value})"


def get_value(value):
    return ord(value) - 96


def can_move_to(value, from_value):
    return value is not None and (get_value(value) - get_value(from_value)) < 2


def find_available_nodes(x, y, elevation_map, visited_pos):
    origin_value = elevation_map[x,y]

    possible_moves = {
        (x, y + 1): elevation_map.get((x, y + 1), None),
        (x, y - 1): elevation_map.get((x, y - 1), None),
        (x + 1, y): elevation_map.get((x + 1, y), None),
        (x - 1, y): elevation_map.get((x - 1, y), None),
    }
    return {k: v for k, v in possible_moves.items() if v is not None and can_move_to(v, origin_value) and k not in visited_pos}


def get_next_node(open_nodes):
    return min(open_nodes.values(), key=lambda x: x.value)


def calculate_path(start_pos, end_pos, elevation_map ):
    visited_nodes = set()
    open_nodes = {start_pos: Node(None, start_pos[0], start_pos[1], 0)}
    at_end = False
    while not at_end:
        if len(open_nodes) == 0:
            return None
        current_node = get_next_node(open_nodes)
        if (current_node.x, current_node.y) == end_pos:
            at_end = True
            continue
        nodes = find_available_nodes(current_node.x, current_node.y, elevation_map, visited_nodes)

        for (x, y), value in nodes.items():
            if (x, y) in open_nodes.keys():
                if open_nodes.get((x, y)).value > current_node.value + 1:
                    print("found quicker way")
                    open_nodes[(x, y)] = Node(current_node, x, y, current_node.value + 1)
            else:
                open_nodes[(x, y)] = Node(current_node, x, y, current_node.value + 1)
        visited_nodes.add((current_node.x, current_node.y))
        open_nodes.pop((current_node.x, current_node.y))

    temp_node = current_node
    i = 0
    path = {end_pos: 'E'}
    while temp_node is not None:
        i += 1
        if temp_node.parent is not None:
            if temp_node.x < temp_node.parent.x:
                path[(temp_node.parent.x, temp_node.parent.y)] = '<'
            elif temp_node.x > temp_node.parent.x:
                path[(temp_node.parent.x, temp_node.parent.y)] = '>'
            elif temp_node.y > temp_node.parent.y:
                path[(temp_node.parent.x, temp_node.parent.y)] = 'v'
            elif temp_node.y < temp_node.parent.y:
                path[(temp_node.parent.x, temp_node.parent.y)] = '^'

        temp_node = temp_node.parent

    # for y in range(len(lines)):
    #     line = []
    #     for x in range(len(lines[y])):
    #         if (x, y) in path.keys():
    #             line.append(path.get((x, y)))
    #         elif (x, y) in visited_nodes:
    #             line.append('o')
    #         else:
    #             line.append('.')
    #
    #     print("".join(line))
    return i-1


start_pos = (0, 0)
end_pos = (0, 0)
a_pos = []
elevation_map = dict()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        raw = lines[y][x]
        if raw == "S":
            start_pos = (x, y)
            elevation_map[(x, y)] = 'a'
        elif raw == "E":
            end_pos = (x, y)
            elevation_map[(x, y)] = 'z'
        elif raw == "a":
            elevation_map[(x, y)] = raw
            a_pos.append((x, y))
        else:
            elevation_map[(x, y)] = raw

shortest_a_path = calculate_path(start_pos, end_pos, elevation_map)
print(f"{start_pos}: {shortest_a_path}")
for start_pos in a_pos:
    result = calculate_path(start_pos, end_pos, elevation_map)
    if result is not None and result < shortest_a_path:
        shortest_a_path = result
        print(f"{start_pos}: {shortest_a_path}")

print(f"Final: {shortest_a_path}")

