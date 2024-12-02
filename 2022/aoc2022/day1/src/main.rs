use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn count_calories() -> Vec<i32> {
    let data = fs::read_to_string("input/day1.txt").expect("Couldn't read file");
    let elves = data.split("\n\n");

    let mut sums: Vec<i32> = Vec::new();

    for elf in elves {
        let mut s: i32 = 0;

        for number in elf.split_terminator("\n") {
            s += number.parse::<i32>().unwrap();
        }

        sums.push(s);
    }

    sums.sort();
    sums.reverse();

    return sums;
}

fn part1() -> i32 {
    let calories = count_calories();

    return calories[0];
}

fn part2() -> i32 {
    let calories = count_calories();

    return calories[0..3].iter().sum::<i32>();
}
