use std::fs;

const CRATE_STACKS: usize = 9;

#[derive(Debug)]
struct Move {
    from: usize,
    to: usize,
    quantity: usize,
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> String {
    let data = fs::read_to_string("input/day5.txt").expect("Couldn't read file");
    let (crates, moves) = data.split_once("\n\n").unwrap();

    let mut crates = parse_crates(crates);
    let moves = parse_moves(moves);

    for mov in moves {
        for _ in 0..mov.quantity {
            let c: char = crates.get_mut(mov.from).expect("From").pop().expect("Pop");
            crates.get_mut(mov.to).unwrap().push(c);
        }
    }

    return crates.iter()
        .map(|stack| stack.last().unwrap().to_owned())
        .collect();
}

fn part2() -> String {
    let data = fs::read_to_string("input/day5.txt").expect("Couldn't read file");
    let (crates, moves) = data.split_once("\n\n").unwrap();

    let mut crates = parse_crates(crates);
    let moves = parse_moves(moves);

    for mov in moves {
        let from = crates.get_mut(mov.from).unwrap();
        let mut tail = from.split_off(from.len() - mov.quantity);
        crates.get_mut(mov.to).unwrap().append(&mut tail);
    }

    return crates.iter()
        .map(|stack| stack.last().unwrap().to_owned())
        .collect();
}

fn parse_crates(crates: &str) -> Vec<Vec<char>> {
    let mut out: Vec<Vec<char>> = Vec::with_capacity(CRATE_STACKS);

    for _ in 0..CRATE_STACKS {
        out.push(Vec::new());
    }

    for line in crates.split("\n") {
        for i in 0..CRATE_STACKS {
            let c: char = line.as_bytes()[1 + i * 4].into();

            if c.is_ascii_uppercase() {
                out[i].insert(0, c);
            }
        }
    }

    return out;
}

fn parse_moves(moves: &str) -> Vec<Move> {
    let mut out: Vec<Move> = Vec::new();

    for line in moves.split_terminator("\n") {
        let words: Vec<&str> = line.split(" ").collect();

        out.push(Move { from: words[3].parse::<usize>().unwrap() - 1, to: words[5].parse::<usize>().unwrap() - 1, quantity: words[1].parse::<usize>().unwrap() });
    }

    return out;
}
