def main():
    # with open(r'C:\Users\DELL\Documents\Extracurricular\Competitive Programming\aoc2022\day18\input_sample.txt') as f:
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

adjacents = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

def part1(lines):
    space = []
    for _ in range(30):
        y_row = []
        for _ in range(30):
            y_row.append(['.'] * 30)
        space.append(y_row)
    result = 0
    for line in lines:
        p = list(map(int, line.split(',')))
        if space[p[0]][p[1]][p[2]] == '#':
            continue
        space[p[0]][p[1]][p[2]] = '#'
        for adj in adjacents:
            if space[p[0] + adj[0]][p[1] + adj[1]][p[2] + adj[2]] == '#':
                result -= 2
        result += 6
    return result

def part2(lines):
    space = []
    size = 25
    for _ in range(size):
        y_row = []
        for _ in range(size):
            y_row.append(['.'] * size)
        space.append(y_row)
    for line in lines:
        p = list(map(lambda x: int(x) + 1, line.split(',')))
        space[p[0]][p[1]][p[2]] = '#'
    to_search = [(0, 0, 0)]
    space[0][0][0] = '_'
    result = 0
    while len(to_search) > 0:
        current = to_search.pop()
        for adjacent in adjacents:
            adj = (current[0] + adjacent[0], current[1] + adjacent[1], current[2] + adjacent[2])
            invalid_adj = False
            for x in adj:
                if x < 0 or x >= size:
                    invalid_adj = True
                    break
            if invalid_adj:
                continue
            if space[adj[0]][adj[1]][adj[2]] == '#':
                result += 1
            elif space[adj[0]][adj[1]][adj[2]] == '.':
                space[adj[0]][adj[1]][adj[2]] = '_'
                to_search.append(adj)
    return result

if __name__ == '__main__':
    main()
