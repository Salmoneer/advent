use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn priority(c: char) -> u8 {
    if c.is_ascii_lowercase() {
        c as u8 - b'a' + 1
    } else if c.is_ascii_uppercase() {
        c as u8 - b'A' + 27
    } else {
        panic!("Non ascii character provided to priority");
    }
}

fn part1() -> u32 {
    let data = fs::read_to_string("input/day3.txt").expect("Couldn't read file");
    let lines = data.split_terminator("\n");

    let mut s: u32 = 0;

    for line in lines {
        let n = line.chars().count();
        let (first_half, second_half) = line.split_at(n / 2);

        for first_c in first_half.chars() {
            if second_half.contains(first_c) {
                s += priority(first_c) as u32;
                break;
            }
        }
    }

    return s;
}

fn part2() -> u32 {
    let data = fs::read_to_string("input/day3.txt").expect("Couldn't read file");
    let lines: Vec<&str> = data.split_terminator("\n").collect();

    let mut s: u32 = 0;

    for i in (0..lines.len()).step_by(3) {
        for first_c in lines[i].chars() {
            if lines[i+1].contains(first_c) && lines[i+2].contains(first_c) {
                s += priority(first_c) as u32;
                break;
            }
        }
    }

    return s;
}
