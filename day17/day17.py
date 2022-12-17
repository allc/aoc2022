from typing import List

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines[0][:-1]))
    print("Part 2:", part2(lines[0][:-1]))

patterns = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

def _move_right(rock, n):
    for i in range(len(rock)):
        p = rock[i]
        rock[i] = (p[0] + n, p[1])

def _move_up(rock, n):
    for i in range(len(rock)):
        p = rock[i]
        rock[i] = (p[0], p[1] + n)

def is_within_width(rock, width):
    for p in rock:
        if p[0] < 0 or p[0] >= width:
            return False
    return True

def is_overlap(rock, bored):
    for p in rock:
        if bored[p[1]][p[0]] == '#':
            return True
    return False

def move_right(rock: List, bored, n):
    next_position = rock.copy()
    _move_right(next_position, n)
    if not is_within_width(next_position, len(bored[0])):
        return rock
    if is_overlap(next_position, bored):
        return rock
    return next_position

def is_above_bottom(rock):
    for p in rock:
        if p[1] < 0:
            return False
    return True

def move_down(rock, bored):
    next_position = rock.copy()
    _move_up(next_position, -1)
    if not is_above_bottom(next_position):
        return rock, False
    if is_overlap(next_position, bored):
        return rock, False
    return next_position, True

def new_rock_fall(i, top, bored, jet: List, jet_step):
    rock = patterns[i % len(patterns)].copy()
    _move_right(rock, 2)
    _move_up(rock, top + 4)
    # print(rock)
    while True:
        j = jet[jet_step % len(jet)]
        jet_step += 1
        if j == '>':
            rock = move_right(rock, bored, 1)
        else:
            rock = move_right(rock, bored, -1)
        # print(rock)
        rock, moved = move_down(rock, bored)
        # print(rock)
        if not moved:
            for p in rock:
                bored[p[1]][p[0]] = '#'
            return rock, jet_step

def part1(line):
    bored = []
    for _ in range(6000):
        bored.append(['.'] * 7)
    top = -1
    jet_step = 0
    for i in range(2022):
        rock, jet_step = new_rock_fall(i, top, bored, line, jet_step)
        for p in rock:
            top = max(top, p[1])
    # for row in bored[::-1]:
    #     print(row)
    return top + 1

def part2(line):
    bored = []
    for _ in range(100000):
        bored.append(['.'] * 7)
    top = -1
    jet_step = 0
    period_counter = dict()
    i = 0
    while True:
        board_top = '' if top < 5 else ''.join([''.join(row) for row in bored[top: top - 5: -1]]) # kinda hacky hmm
        period_counter_key = (i % len(patterns), jet_step % len(line), board_top)
        if period_counter_key in period_counter:
            period = i - period_counter[period_counter_key]
            break
        period_counter[(i % len(patterns), jet_step % len(line), board_top)] = i
        rock, jet_step = new_rock_fall(i, top, bored, line, jet_step)
        for p in rock:
            top = max(top, p[1])
        i += 1
    last_top = top
    for _ in range(period):
        rock, jet_step = new_rock_fall(i, top, bored, line, jet_step)
        for p in rock:
            top = max(top, p[1])
        i += 1
    diff = top - last_top
    last_top = top
    for _ in range(period):
        rock, jet_step = new_rock_fall(i, top, bored, line, jet_step)
        for p in rock:
            top = max(top, p[1])
        i += 1
    diff = top - last_top
    last_top = top
    for _ in range((1000000000000 - i) % period):
        rock, jet_step = new_rock_fall(i, top, bored, line, jet_step)
        for p in rock:
            top = max(top, p[1])
        i += 1
    return top + 1 + (1000000000000 - i) // period * diff

if __name__ == '__main__':
    main()
