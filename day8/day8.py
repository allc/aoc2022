def main():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        grid.append(list(map(int, line[:-1])))
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))

def part1(grid):
    num_visible = 0
    is_visible = []
    for _ in range(len(grid)):
        is_visible.append([False] * len(grid[0]))
    for i in range(1, len(grid) - 1):
        # left to right for each row
        tallest = grid[i][0]
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] > tallest:
                tallest = grid[i][j]
                if not is_visible[i][j]:
                    num_visible += 1
                    is_visible[i][j] = True
        # right to left for each row
        tallest = grid[i][len(grid[0]) - 1]
        for j in range(len(grid[0]) - 2, 0, -1):
            if grid[i][j] > tallest:
                tallest = grid[i][j]
                if not is_visible[i][j]:
                    num_visible += 1
                    is_visible[i][j] = True
    for j in range(1, len(grid[0]) - 1):
        # top to bottom for each col
        tallest = grid[0][j]
        for i in range(1, len(grid) - 1):
            if grid[i][j] > tallest:
                tallest = grid[i][j]
                if not is_visible[i][j]:
                    num_visible += 1
                    is_visible[i][j] = True
        # bottom to top for each col
        tallest = grid[len(grid) - 1][j]
        for i in range(len(grid) - 2, 0, -1):
            if grid[i][j] > tallest:
                tallest = grid[i][j]
                if not is_visible[i][j]:
                    num_visible += 1
                    is_visible[i][j] = True
    # for a in is_visible:
    #     print(a)
    return num_visible + len(grid) * 2 + (len(grid[0]) - 2) * 2

def part2(grid):
    h = len(grid)
    w = len(grid[0])
    highest_score = 0
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            current_score = 1
            # look up
            for k in range(i - 1, -1, -1):
                if grid[i][j] <= grid[k][j]:
                    break
            current_score *= i - k
            # look down
            for k in range(i + 1, h):
                if grid[i][j] <= grid[k][j]:
                    break
            current_score *= k - i
            # look left
            for k in range(j - 1, -1, -1):
                if grid[i][j] <= grid[i][k]:
                    break
            current_score *= j - k
            # look right
            for k in range(j + 1, w):
                if grid[i][j] <= grid[i][k]:
                    break
            current_score *= k - j
            highest_score = max(highest_score, current_score)
    return highest_score

if __name__ == '__main__':
    main()
