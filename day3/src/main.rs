use std::{fs, iter::Peekable, str::Lines};
use log::{debug};
use std::collections::HashSet;

fn main() {
    simple_logger::init_with_level(log::Level::Debug).unwrap();
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");
    println!("Part 1: {}", part_1(&contents));
    println!("Part 2: {}", part_2(&contents));
}

fn item_to_priority(item: char) -> u32 {
    match item {
        item if item.is_lowercase() => item as u32 - 96,
        item if item.is_uppercase() => item as u32 - 64 + 26,
        _ => 0,
    }
}

fn get_rucksack_priority(rucksack: &str) -> u32 {
    let mut items = vec![0; 53];
    let item_count = rucksack.chars().count();
    debug!("Item count: {item_count}");
    debug!("item_count / 2: {}", item_count / 2);
    for c in rucksack[0..item_count / 2].chars() {
        // debug!("First compartment: {c}");
        let priority = item_to_priority(c);
        items[priority as usize] = 1;
    }
    debug!("Items: {:?}", items);
    for c in rucksack[item_count / 2..item_count].chars() {
        // debug!("Second compartment: {c}");
        let priority = item_to_priority(c);
        if items[priority as usize] > 0 {
            debug!("Priority: {priority}({c})");
            return priority;
        }
    }
    0
}

fn part_1(contents: &String) -> u32 {
    let mut total_priorities = 0;
    let lines = contents.lines();
    for line in lines {
        total_priorities += get_rucksack_priority(line);
    }
    total_priorities
}

fn get_group_priority(rucksacks: &mut Peekable<Lines>) -> u32 {
    let mut items = vec![0; 53];
    let next_line = rucksacks.peek().unwrap();
    debug!("Next line: {next_line}");
    for c in HashSet::<char>::from_iter(rucksacks.next().unwrap().chars()) {
        let priority = item_to_priority(c);
        items[priority as usize] += 1;
    }
    debug!("Items: {:?}", items);
    let next_line = rucksacks.peek().unwrap();
    debug!("Next line: {next_line}");
    for c in HashSet::<char>::from_iter(rucksacks.next().unwrap().chars()) {
        let priority = item_to_priority(c);
        items[priority as usize] += 1;
    }
    debug!("Items: {:?}", items);
    let next_line = rucksacks.peek().unwrap();
    debug!("Next line: {next_line}");
    for c in rucksacks.next().unwrap().chars() {
        let priority = item_to_priority(c);
        if items[priority as usize] > 1 {
            return priority;
        }
    }
    0
}

fn part_2(contents: &String) -> u32 {
    let mut total_priorities = 0;
    let lines = contents.lines();
    let mut line_iter = lines.peekable();
    while !line_iter.peek().is_none() {
        total_priorities += get_group_priority(&mut line_iter);
    }
    total_priorities
}
