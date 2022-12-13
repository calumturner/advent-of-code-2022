from typing import List

with open("test.txt") as f:
    lines = f.read().splitlines()

start_pos = (0, 0)
end_pos = (0, 0)

elevation_map = dict()


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"Point(({self.x}, {self.y})), {self.value}({self.get_value()}))"

    def get_value(self):
        return ord(self.value) - 96

    def can_move_to(self, from_point):
        return self.value is not None and self.get_value() - from_point.get_value() in [0, 1]


def find_available_points(x, y, elevation_map, visited_pos):
    origin_value = elevation_map[x,y]

    possible_moves = {
        (x, y + 1): elevation_map.get((x, y + 1), None),
        (x, y - 1): elevation_map.get((x, y - 1), None),
        (x + 1, y): elevation_map.get((x + 1, y), None),
        (x - 1, y): elevation_map.get((x - 1, y), None),
    }
    return {k: v for k, v in possible_moves.items() if v is not None and v.can_move_to(origin_value) and v not in visited_pos}


for y in range(len(lines)):
    for x in range(len(lines[y])):
        raw = lines[y][x]
        if raw == "S":
            start_pos = (x, y)
            elevation_map[(x, y)] = Point(x, y, 'a')
        elif raw == "E":
            end_pos = (x, y)
            elevation_map[(x, y)] = Point(x, y, 'z')
        else:
            elevation_map[(x, y)] = Point(x, y, raw)

visited_pos = {elevation_map.get(start_pos)}
current_position = elevation_map.get(start_pos)
at_destination = False

possible_points = find_available_points(current_position, elevation_map, visited_pos, 1)


def find_min_next_point(possible_points):
    return []


current_position = find_min_next_point(possible_points)


# paths = [{'moves': move, 'total': 1 + move.get_value(), 'available_moves': {}} for k, move in find_available_moves(current_position, elevation_map).items()]
while not at_destination:
    # available_moves = dict()
    # for path in paths:
    #     path_head = path.get('moves')[0]
    #     path_moves = find_available_moves(path_head, elevation_map, visited_pos)
    #     if len(path_moves) == 0:
    #         paths.remove(path)
    #     for new_move in path_moves:
    #         paths.append({'moves': [new_move]+path.get('moves'),
    #                       'total': path.get("total"),
    #                       })





    print()





print()
