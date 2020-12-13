use std::fs;

fn main() {
    part1_procedural();
    part1_functional();
}

fn part1_functional() {
    let numbers: Vec<i32> = fs::read_to_string("../inputs/day1.txt")
        .expect("Failed to open file!")
        .split('\n')
        .map(|s| s.parse().unwrap())
        .collect();

    calc_part1_functional(&numbers)
}

// JK, don't know how to make this functional
fn calc_part1_functional(numbers: &Vec<i32>) {
    for n1 in numbers {
        for n2 in numbers {
            if n1 + n2 == 2020 {
                println!("Answer: {}", n1 * n2);
                return;
            }
        }
    }
}

fn part1_procedural() {
    let contents = fs::read_to_string("../inputs/day1.txt").expect("Failed to open file!");

    let mut numbers: Vec<i32> = vec![];
    for string in contents.split_whitespace() {
        numbers.push(string.parse().unwrap());
    }
    for n1 in &numbers {
        for n2 in &numbers {
            if n1 + n2 == 2020 {
                println!("Answer: {}", n1 * n2);
                return;
            }
        }
    }
}
