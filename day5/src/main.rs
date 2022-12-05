use std::fs;
use std::collections::VecDeque;
use log::{debug};

fn main() {
    simple_logger::init_with_level(log::Level::Debug).unwrap();
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");

    let mut lines = contents.lines();
    let mut line = lines.next().unwrap();
    let num_stacks = (line.chars().count() + 1) / 4;
    let mut stacks: Vec<VecDeque<char>> = Vec::with_capacity(num_stacks);
    for _ in 0..num_stacks {
        stacks.push(VecDeque::new());
    }
    process_stacks_line(line, &mut stacks);
    debug!("Stacks: {:?}", stacks);
    loop {
        line = lines.next().unwrap();
        if line.chars().next().unwrap() != '[' {
            break;
        }
        process_stacks_line(line, &mut stacks);
    }
    debug!("Stacks: {:?}", stacks);

    lines.next();
    let mut moves: Vec<(u32, u32, u32)> = Vec::new();
    loop {
        let line = lines.next();
        match line {
            Some(l) => {
                let m = parse_move(l);
                moves.push(m);
            },
            None => break,
        }
    }
    let stacks_1 = stacks.clone();
    println!("Part 1: {}", part_1(stacks_1, &moves));
    let stacks_2 = stacks.clone();
    println!("Part 2: {}", part_2(stacks_2, &moves));
}

fn process_stacks_line(line: &str, stacks: &mut Vec<VecDeque<char>>) {
    for i in 0..stacks.len() {
        let j = 4 * i + 1;
        let crat = line.chars().nth(j).unwrap();
        if crat != ' ' {
            stacks[i].push_front(crat);
        }
    }
}

fn parse_move(line: &str) -> (u32, u32, u32) {
    let line_split: Vec<&str> = line.split(" ").collect();
    let mov: u32 = line_split[1].parse().unwrap();
    let from: u32 = line_split[3].parse().unwrap();
    let to: u32 = line_split[5].parse().unwrap();
    (mov, from, to)
}

fn part_1(mut stacks: Vec<VecDeque<char>>, moves: &Vec<(u32, u32, u32)>) ->
    String 
{
    for (mov, from, to) in moves {
        let (mov, from, to) = (*mov, *from, *to);
        for _ in 0..mov {
            let crat = &stacks[from as usize - 1].pop_back().unwrap();
            stacks[to as usize - 1].push_back(*crat);
        }
    }
    debug!("Part 1 stacks: {:?}", stacks);
    let tops: String = stacks.iter().map(|x| *x.back().unwrap()).collect();
    tops
}

fn part_2(mut stacks: Vec<VecDeque<char>>, moves: &Vec<(u32, u32, u32)>) ->
    String
{
    for (mov, from, to) in moves {
        let (mov, from, to) = (*mov, *from, *to);
        let from_stack_new_len = stacks[from as usize - 1].len() - mov as usize;
        let crats: Vec<char> = stacks[from as usize - 1].drain(from_stack_new_len..).collect();
        stacks[to as usize - 1].extend(crats);
    }
    debug!("Part 1 stacks: {:?}", stacks);
    let tops: String = stacks.iter().map(|x| *x.back().unwrap()).collect();
    tops
}
