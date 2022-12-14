from functools import cmp_to_key

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def get_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

class Cave:
    def __init__(self, cave, source, bottom_most):
        self.cave = cave
        self.source = source
        self.bottom_most = bottom_most

def build_rock(cave: Cave, rock):
    for a, b in zip(rock[:-1], rock[1:]):
        a_x, a_y = a
        b_x, b_y = b
        if a_x == b_x:
            sign = get_sign(b_y - a_y)
            for y in range(a_y, b_y + sign, sign):
                cave.cave[y][a_x] = '#'
                if a_x == 500:
                    cave.source = min(cave.source, y - 1)
                cave.bottom_most = max(cave.bottom_most, y)
        elif a_y == b_y:
            sign = get_sign(b_x - a_x)
            for x in range(a_x, b_x + sign, sign):
                cave.cave[a_y][x] = '#'
                if x == 500:
                    cave.source = min(cave.source, a_y - 1)
            cave.bottom_most = max(cave.bottom_most, a_y)

def build_cave(lines, width=570):
    cave = []
    source = 1000
    bottom_most = 0
    for _ in range(165):
        cave.append(['.'] * width)
    cave = Cave(cave, source, bottom_most)
    for line in lines:
        line = line.split(' -> ')
        line = [tuple(map(int, coord.split(','))) for coord in line]
        build_rock(cave, line)
    return cave

def step(cave: Cave, current):
    x, y = current
    if cave.cave[y + 1][x] == '.':
        # print('Moving down')
        current = (x, y + 1)
    elif cave.cave[y + 1][x - 1] == '.':
        current = (x - 1, y + 1)
    elif cave.cave[y + 1][x + 1] == '.':
        current = (x + 1, y + 1)
    return current

def produce(cave: Cave):
    # print('Producing')
    current = (500, cave.source)
    while True:
        new_current = step(cave, current)
        if new_current == current:
            cave.cave[current[1]][current[0]] = 'O'
            if current == (500, cave.source):
                cave.source -= 1
                if cave.source < 0:
                    return True
            return False
        if new_current[1] >= cave.bottom_most:
            return True
        current = new_current

def part1(lines):
    cave = build_cave(lines)
    print('\n'.join([''.join(row[480:]) for row in cave.cave[10:]]))
    print()
    finished = False
    result = 0
    while not finished:
        finished = produce(cave)
        result += 1
    print('\n'.join([''.join(row[480:]) for row in cave.cave[10:]]))
    return result - 1

def part2(lines):
    cave = build_cave(lines, 770)
    cave.bottom_most += 2
    cave.cave[cave.bottom_most] = ['#'] * len(cave.cave[0])
    print('\n'.join([''.join(row[480:630]) for row in cave.cave[10:]]))
    print()
    finished = False
    result = 0
    while not finished:
        finished = produce(cave)
        result += 1
    print('\n'.join([''.join(row[480:630]) for row in cave.cave[10:]]))
    return result

if __name__ == '__main__':
    main()
