use std::fs;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let data = fs::read_to_string("input/day4.txt").expect("Couldn't read file");
    let lines = data.split_terminator("\n");

    let mut s: u32 = 0;

    for line in lines {
        let (first_elf_data, second_elf_data) = line.split_once(",").expect("Couldn't split line on `,`");

        let first_elf_data = first_elf_data.split_once("-").expect("Couldn't split first elf on `-`");
        let second_elf_data = second_elf_data.split_once("-").expect("Couldn't split second elf on `-`");

        let (first_elf_start, first_elf_end) = (first_elf_data.0.parse::<u32>().unwrap(), first_elf_data.1.parse::<u32>().unwrap());
        let (second_elf_start, second_elf_end) = (second_elf_data.0.parse::<u32>().unwrap(), second_elf_data.1.parse::<u32>().unwrap());

        if (first_elf_start <= second_elf_start && first_elf_end >= second_elf_end) ||
           (second_elf_start <= first_elf_start && second_elf_end >= first_elf_end) {
            s += 1;
        }
    }

    return s;
}

// I learnt rust in here

fn part2() -> u32 {
    let data = fs::read_to_string("input/day4.txt").expect("Couldn't read file");
    let lines = data.split_terminator("\n");

    let mut s: u32 = 0;

    for line in lines {
        let elf: Vec<Vec<u32>> = line.split(",")
            .map(|data|data.split("-")
                .map(|x| x.parse::<u32>().unwrap())
                .collect())
            .collect();

        if !(elf[0][1] < elf[1][0] || elf[1][1] < elf[0][0]) {
            s += 1;
        }
    }

    return s;
}
