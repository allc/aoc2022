use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read input file");
    println!("Part 1: {}", part_1(&contents));
    println!("Part 2: {}", part_2(&contents));
}

fn part_1(contents: &String) -> i32 {
    let action_scoring = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);
    let win_list = HashMap::from([
        ("C", "X"),
        ("A", "Y"),
        ("B", "Z"),
    ]);
    let draw_list = HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z"),
    ]);

    let mut score = 0;
    let lines = contents.lines();
    for line in lines {
        let line_split: Vec<&str> = line.split(" ").collect();
        let opponent = line_split[0];
        let strategy = line_split[1];
        score += action_scoring[strategy];
        if win_list[opponent] == strategy {
            score += 6;
        } else if draw_list[opponent] == strategy {
            score += 3;
        }
    }
    score
}

fn part_2(contents: &String) -> i32 {
    let win_scoring = HashMap::from([
        ("A", 2),
        ("B", 3),
        ("C", 1),
    ]);
    let draw_scoring = HashMap::from([
        ("A", 1),
        ("B", 2),
        ("C", 3),
    ]);
    let lose_scoring = HashMap::from([
        ("A", 3),
        ("B", 1),
        ("C", 2),
    ]);
    let strategy_scoring = HashMap::from([
        ("X", 0),
        ("Y", 3),
        ("Z", 6),
    ]);

    let mut score = 0;
    let lines = contents.lines();
    for line in lines {
        let line_split: Vec<&str> = line.split(" ").collect();
        let opponent = line_split[0];
        let strategy = line_split[1];
        score += strategy_scoring[strategy];
        match strategy {
            "X" => score += lose_scoring[opponent],
            "Y" => score += draw_scoring[opponent],
            "Z" => score += win_scoring[opponent],
            _ => (),
        }
    }
    score
}
