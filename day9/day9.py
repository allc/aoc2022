from functools import cmp_to_key

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def move_head(head, direction):
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'L':
        head[0] -= 1
    elif direction == 'R':
        head[0] += 1

def get_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def follow_tail(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return
    if head_y != tail_y:
        tail[1] += get_sign(head_y - tail_y)
    if head_x != tail_x:
        tail[0] += get_sign(head_x - tail_x)

def part1(lines):
    head = [0] * 2
    tail = [0] * 2
    visited = set([tuple(tail)])
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            move_head(head, direction)
            follow_tail(head, tail)
            visited.add(tuple(tail))
    return len(visited)

def part2(lines):
    rope = []
    for _ in range(10):
        rope.append([0] * 2)
    visited = set([tuple(rope[-1])])
    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            move_head(rope[0], direction)
            for i in range(len(rope) - 1):
                follow_tail(rope[i], rope[i + 1])
            visited.add(tuple(rope[-1]))
    return len(visited)

if __name__ == '__main__':
    main()
