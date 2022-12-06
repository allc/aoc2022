use std::fs;
use std::collections::HashSet;
use log::debug;

fn main() {
    simple_logger::init_with_level(log::Level::Debug).unwrap();
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");
    println!("Part 1: {}", part_1(&contents));
    println!("Part 2: {}", part_2(&contents));
}

fn find_marker(contents: &String, len: usize) -> Option<usize> {
    for i in 0..contents.chars().count() - len {
        let sequence = &contents[i..i + len];
        let set: HashSet<char> = HashSet::from_iter(sequence.chars());
        // debug!("Set: {:?}", set);
        if set.len() == len {
            return Some(i);
        }
    }
    None
}

fn part_1(contents: &String) -> usize {
    find_marker(contents, 4).unwrap() + 4
}

fn part_2(contents: &String) -> usize {
    find_marker(contents, 14).unwrap() + 14
}
