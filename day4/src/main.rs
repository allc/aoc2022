use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");
    println!("Part 1: {}", part_1(&contents));
    println!("Part 2: {}", part_2(&contents));
}

fn part_1(contents: &String) -> i32 {
    let mut result = 0;
    let lines = contents.lines();
    for line in lines {
        let pairs: Vec<&str> = line.split(",").collect();
        let elf1: Vec<i32> = pairs[0].split("-").map(|x| x.parse().unwrap()).collect();
        let elf2: Vec<i32> = pairs[1].split("-").map(|x| x.parse().unwrap()).collect();
        if elf1[0] >= elf2[0] && elf1[1] <= elf2[1] || elf2[0] >= elf1[0] && elf2[1] <= elf1[1] {
            result += 1;
        }
    }
    result
}

fn part_2(contents: &String) -> i32 {
    let mut result = 0;
    let lines = contents.lines();
    for line in lines {
        let pairs: Vec<&str> = line.split(",").collect();
        let elf1: Vec<i32> = pairs[0].split("-").map(|x| x.parse().unwrap()).collect();
        let elf2: Vec<i32> = pairs[1].split("-").map(|x| x.parse().unwrap()).collect();
        if elf1[0] >= elf2[0] && elf1[0] <= elf2[1] || elf2[0] >= elf1[0] && elf2[0] <= elf1[1] {
            result += 1;
        }
    }
    result
}
