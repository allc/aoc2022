from typing import List
import math

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

class Monkey:
    def __init__(self, items, operator, operand, test, true_target, false_target):
        self.n_inspect = 0
        self.items: List[int] = items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.true_target = true_target
        self.false_target = false_target

    def act(self, reduce_worry=True):
        throws = []
        for item in self.items:
            self.n_inspect += 1
            if self.operator == '*':
                if self.operand == 'old':
                    item *= item
                else:
                    item *= self.operand
            elif self.operator == '+':
                if self.operand == 'old':
                    item += item
                else:
                    item += self.operand
            if reduce_worry:
                item //= 3
            if item % self.test == 0:
                target = self.true_target
            else:
                target = self.false_target
            throws.append((item, target))
        self.items = []
        return throws

    def add_item(self, item):
        self.items.append(item)

def get_monkeys(lines):
    monkeys = []
    lines_iter = iter(lines)
    for _ in range((len(lines) + 1) // 7):
        next(lines_iter)

        items = list(map(int, next(lines_iter).split(': ')[-1].split(', ')))

        op_str = next(lines_iter).split('old ')[-1].split()
        operator = op_str[0]
        if op_str[1] == 'old':
            operand = op_str[1]
        else:
            operand = int(op_str[1])

        test = int(next(lines_iter).split('by ')[-1])

        true_target = int(next(lines_iter).split('monkey ')[-1])

        false_target = int(next(lines_iter).split('monkey ')[-1])

        monkeys.append(Monkey(items, operator, operand, test, true_target, false_target))
        try:
            next(lines_iter)
        except StopIteration:
            break
    return monkeys

def part1(lines):
    monkeys: List[Monkey] = get_monkeys(lines)
    for i in range(20):
        for monkey in monkeys:
            throws = monkey.act()
            for throw in throws:
                monkeys[throw[1]].add_item(throw[0])
    # print(i, [monkey.n_inspect for monkey in monkeys])
    largest = 0
    second_largest = 0
    for monkey in monkeys:
        if monkey.n_inspect > second_largest:
            second_largest = monkey.n_inspect
            if second_largest > largest:
                tmp = largest
                largest = second_largest
                second_largest = tmp
    return largest * second_largest

def part2(lines):
    monkeys: List[Monkey] = get_monkeys(lines)
    test_lcm = math.lcm(*[monkey.test for monkey in monkeys])
    for i in range(10000):
        for monkey in monkeys:
            throws = monkey.act(False)
            for throw in throws:
                monkeys[throw[1]].add_item(throw[0] % test_lcm)
    # print(i, [monkey.n_inspect for monkey in monkeys])
    largest = 0
    second_largest = 0
    for monkey in monkeys:
        if monkey.n_inspect > second_largest:
            second_largest = monkey.n_inspect
            if second_largest > largest:
                tmp = largest
                largest = second_largest
                second_largest = tmp
    return largest * second_largest

if __name__ == '__main__':
    main()
