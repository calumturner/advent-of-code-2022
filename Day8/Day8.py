
from functools import reduce

with open("input.txt") as f:
    lines = f.read().splitlines()

trees = [list(row) for row in lines]


def isTreeVisible(x, y, trees):
    if (x < 1 or x > len(trees)-2) or (y < 1 or y > len(trees)-2):
        return True

    is_tree_visible_from_right = trees[x][y+1:]
    if max(is_tree_visible_from_right) < trees[x][y]:
        return True

    is_tree_visible_from_left = trees[x][:y]
    if max(is_tree_visible_from_left) < trees[x][y]:
        return True

    is_tree_visible_from_top = [t[y] for t in trees[:x]]
    if max(is_tree_visible_from_top) < trees[x][y]:
        return True

    is_tree_visible_from_bottom = [t[y] for t in trees[x+1:]]
    if max(is_tree_visible_from_bottom) < trees[x][y]:
        return True


def calculate_scenic_score(cur_tree, trees):
    if len(trees) == 0:
        return 0

    distance = 0
    for tree in trees:
        distance += 1
        if tree >= cur_tree:
            return distance
    return distance


def howFarCanISee(x, y, trees):
    cur_tree = trees[x][y]
    is_tree_visible_from_right = trees[x][y + 1:]
    is_tree_visible_from_left = trees[x][:y]
    is_tree_visible_from_left.reverse()
    is_tree_visible_from_top = [t[y] for t in trees[:x]]
    is_tree_visible_from_top.reverse()
    is_tree_visible_from_bottom = [t[y] for t in trees[x + 1:]]

    values = [x for x in [
        calculate_scenic_score(cur_tree, is_tree_visible_from_right),
        calculate_scenic_score(cur_tree, is_tree_visible_from_left),
        calculate_scenic_score(cur_tree, is_tree_visible_from_top),
        calculate_scenic_score(cur_tree, is_tree_visible_from_bottom)]
                if x > 0]

    return reduce(lambda x, y: x * y, values)



visible_trees = []
for row_index in range(1, len(trees)-1):
    for column_index in range(1, len(trees)-1):
            if isTreeVisible(row_index, column_index, trees):
                visible_trees.append((row_index, column_index))

print(len(visible_trees) + (len(trees)*2) + ((len(trees)-2) * 2))

scores = []
for row_index in range(0, len(trees)):
    for column_index in range(0, len(trees)):
        scores.append(howFarCanISee(row_index, column_index, trees))

print(scores)
print(max(scores))
