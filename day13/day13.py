from functools import cmp_to_key

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r
    if isinstance(l, int):
        return compare([l], r)
    if isinstance(r, int):
        return compare(l, [r])
    for i in range(min(len(l), len(r))):
        result = compare(l[i], r[i])
        if result != 0:
            return result
    return len(l) - len(r)

def parse_packet(line):
    stack = []
    current = None
    num = ''
    for c in line:
        if c == '[':
            new_list = []
            if current is not None:
                current.append(new_list)
                stack.append(current)
            current = new_list
        elif c == ']':
            if num != '':
                current.append(int(num))
                num = ''
            if len(stack) > 0:
                current = stack.pop()
        elif c == ',':
            if num != '':
                current.append(int(num))
                num = ''
        else:
            num += c
    return current

def part1(lines):
    result = 0
    i = 0
    while i < len(lines):
        l = lines[i]
        r = lines[i + 1]
        l = parse_packet(l)
        r = parse_packet(r)
        cmp_result = compare(l, r)
        if cmp_result < 0:
            result += i // 3 + 1
        i += 3
    return result

def part2(lines):
    packets = [parse_packet(line) for line in lines if line != '\n']
    i1 = 1
    for packet in packets:
        if compare(packet, [[2]]) < 0:
            i1 += 1
    i2 = 2
    for packet in packets:
        if compare(packet, [[6]]) < 0:
            i2 += 1
    return i1 * i2

if __name__ == '__main__':
    main()
