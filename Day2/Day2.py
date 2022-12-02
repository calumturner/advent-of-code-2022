

with open("input.txt") as f:
    guide = [line.split(' ') for line in f.read().splitlines()]

rock = 'A'
paper = 'B'
scissors = 'C'

play_rock = 'X'
play_paper = 'Y'
play_scissors = 'Z'

move_map = {
    play_rock: rock,
    play_paper: paper,
    play_scissors: scissors
}

score_map = {
    rock: 1,
    paper: 2,
    scissors: 3
}

winning_moves = {
    rock: scissors,
    scissors: paper,
    paper: rock
}

losing_moves = dict(zip(winning_moves.values(), winning_moves.keys()))

score_draw = 3
score_win = 6

lose = 'X'
draw = 'Y'
win = 'Z'

def calculate_score(opponent_move, my_move):
    if opponent_move == my_move:
        return score_draw + score_map.get(opponent_move)

    if winning_moves.get(my_move) == opponent_move:
        return score_win + score_map.get(my_move)

    return score_map.get(my_move)


def calculate_score_part2(opponent_move, outcome):
    if outcome == draw:
        return score_draw + score_map.get(opponent_move)

    if outcome == lose:
        return score_map.get(winning_moves.get(opponent_move))

    return score_win + score_map.get(losing_moves.get(opponent_move))


def part1(guide):
    normalised_moves = [(move[0], move_map.get(move[1])) for move in guide]
    total = sum([calculate_score(move[0], move[1]) for move in normalised_moves])
    print(f"Part 1 total: {total}")


def part2(guide):
    total = sum([calculate_score_part2(move[0], move[1]) for move in guide])
    print(f"Part 2 total: {total}")


part1(guide)
print()
part2(guide)