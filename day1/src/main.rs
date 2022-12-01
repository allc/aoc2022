use std::fs;
use std::cmp::max;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");
    println!("Part 1: {}", part_1(&contents));
    println!("Part 2: {}", part_2(&contents));
}

fn part_1(contents: &String) -> i32 {
    let lines = contents.lines();
    let mut most = 0;
    let mut current = 0;
    for line in lines {
        match line {
            "" => {
                most = max(current, most);
                current = 0;
            },
            _ => current += line.parse::<i32>().unwrap(),
        }
    }
    most = max(current, most);
    most
}

struct TopThree {
    parent: i32,
    left: i32,
    right: i32,
}

impl TopThree {
    fn insert(&mut self, n: i32) {
        if n > self.parent {
            if n >= self.right {
                self.left = self.parent;
                self.parent = self.right;
                self.right = n;
            } else {
                self.left = self.parent;
                self.parent = n;
            }
        } else {
            self.left = max(self.left, n);
        }
    }

    fn sum(self) -> i32 {
        self.parent + self.left + self.right
    }
}

fn part_2(contents: &String) -> i32 {
    let lines = contents.lines();
    let mut top_three = TopThree { parent: 0, left: 0, right: 0 };
    let mut current = 0;
    for line in lines {
        match line {
            "" => {
                top_three.insert(current);
                current = 0;
            },
            _ => current += line.parse::<i32>().unwrap(),
        }
    }
    top_three.insert(current);
    top_three.sum()
}
