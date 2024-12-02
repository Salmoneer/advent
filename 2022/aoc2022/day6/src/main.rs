use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> usize {
    let data = fs::read_to_string("input/day6.txt").expect("Couldn't read file");

    return find_unique(&data, 4).expect("Couldn't find unique string");
}

fn part2() -> usize {
    let data = fs::read_to_string("input/day6.txt").expect("Couldn't read file");

    return find_unique(&data, 14).expect("Couldn't find unique string");
}

fn find_unique(data: &str, n: usize) -> Option<usize> {
    for i in n..data.len() {
        if unique(&data[i-n..i]) {
            return Some(i);
        }
    }

    return None;
}

fn unique(chars: &str) -> bool {
    for i in 0..chars.len() {
        for j in 0..chars.len() {
            if i != j && chars.chars().nth(i) == chars.chars().nth(j) {
                return false;
            }
        }
    }

    return true;
}
