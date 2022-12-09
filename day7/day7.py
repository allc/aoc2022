def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = dict()
        self.size = None

def build_file_tree(lines):
    root = Directory("/", None)
    current = root
    for line in lines[1:]:
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    current = current.parent
                else:
                    current = current.contents[line[2]]
        else:
            if line[1] not in current.contents:
                if line[0] == 'dir':
                    current.contents[line[1]] = Directory(line[1], current)
                else:
                    current.contents[line[1]] = File(line[1], int(line[0]), current)
    return root

def part1(lines):
    root = build_file_tree(lines)
    result = 0
    stack = [root]
    while len(stack) > 0:
        current = stack[-1]
        can_determine_size = True
        size = 0
        for _, child in current.contents.items():
            if isinstance(child, File):
                size += child.size
            else:
                if child.size is not None:
                    size += child.size
                else:
                    stack.append(child)
                    can_determine_size = False
        if can_determine_size:
            current.size = size
            if size <= 100000:
                result += size
            stack.pop()
    return result

def part2(lines):
    root = build_file_tree(lines)
    stack = [root]
    while len(stack) > 0:
        current = stack[-1]
        can_determine_size = True
        size = 0
        for _, child in current.contents.items():
            if isinstance(child, File):
                size += child.size
            else:
                if child.size is not None:
                    size += child.size
                else:
                    stack.append(child)
                    can_determine_size = False
        if can_determine_size:
            current.size = size
            stack.pop()
    unused = 70000000 - root.size
    required = 30000000 - unused
    smallest = root.size
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if current.size >= required:
            smallest = min(smallest, current.size)
        for _, child in current.contents.items():
            if isinstance(child, Directory):
                stack.append(child)
    return smallest

if __name__ == '__main__':
    main()
