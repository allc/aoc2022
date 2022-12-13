def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print('Part 1:', part1(lines))
    print('Part 2:\n{}'.format(part2(lines)))

def part1(lines):
    result = 0
    x = 1
    cycle = 0
    last_cycle = 0
    for line in lines:
        if line[0] == 'a':
            x += int(line.split()[1])
            cycle += 2
        else:
            cycle += 1
        if cycle < 220:
            if (cycle - 19) % 40 == 0 and cycle != last_cycle:
                result += (cycle + 1) * x
            elif (cycle - 18) % 40 == 0:
                result += (cycle + 2) * x
                last_cycle = cycle + 1
    return result

def draw(screen, cycle, x):
    row = cycle // 40
    position = cycle % 40
    if position >= x - 1 and position <= x + 1:
        screen[row].append('#')
    else:
        screen[row].append('.')

def part2(lines):
    screen = []
    for _ in range(6):
        screen.append([])
    cycle = 0
    x = 1
    for line in lines:
        draw(screen, cycle, x)
        cycle += 1
        if line[0] == 'a':
            draw(screen, cycle, x)
            x += int(line.split()[1])
            cycle += 1
    screen = [''.join(row) for row in screen]
    return '\n'.join(screen)

if __name__ == '__main__':
    main()
