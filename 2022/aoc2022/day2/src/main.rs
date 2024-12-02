use std::fs;

#[derive(PartialEq)]
enum RPS {
    Rock,
    Paper,
    Scissors
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn score_games(games: Vec<(RPS, RPS)>) -> i32 {
    let mut s: i32 = 0;

    for game in games {
        let opponent = game.0;
        let player = game.1;

        if opponent == RPS::Rock     && player == RPS::Paper
        || opponent == RPS::Paper    && player == RPS::Scissors
        || opponent == RPS::Scissors && player == RPS::Rock {
            s += 6;
        } else if opponent == player {
            s += 3;
        }

        s += player as i32 + 1;
    }

    return s;
}

fn part1() -> i32 {
    let data = fs::read_to_string("input/day2.txt").expect("Couldn't read file");
    let lines = data.split_terminator("\n");

    let mut games: Vec<(RPS, RPS)> = Vec::new();

    for line in lines {
        let opponent = match line.as_bytes()[0] {
            b'A' => RPS::Rock,
            b'B' => RPS::Paper,
            b'C' => RPS::Scissors,
            _ => panic!("Couldn't convert opponent's move"),
        };

        let player = match line.as_bytes()[2] {
            b'X' => RPS::Rock,
            b'Y' => RPS::Paper,
            b'Z' => RPS::Scissors,
            _ => panic!("Couldn't convert opponent's move"),
        };

        games.push((opponent, player));
    }

    return score_games(games);
}

fn part2() -> i32 {
    let data = fs::read_to_string("input/day2.txt").expect("Couldn't read file");
    let lines = data.split_terminator("\n");

    let mut games: Vec<(RPS, RPS)> = Vec::new();

    for line in lines {
        let opponent = match line.as_bytes()[0] {
            b'A' => RPS::Rock,
            b'B' => RPS::Paper,
            b'C' => RPS::Scissors,
            _ => panic!("Couldn't convert opponent's move"),
        };

        let player = match line.as_bytes()[2] {
            b'X' => match opponent {
                RPS::Rock => RPS::Scissors,
                RPS::Paper => RPS::Rock,
                RPS::Scissors => RPS::Paper,
            },
            b'Y' => match line.as_bytes()[0] {
                b'A' => RPS::Rock,
                b'B' => RPS::Paper,
                b'C' => RPS::Scissors,
                _ => panic!("Couldn't convert opponent's move"),
            },
            b'Z' => match opponent {
                RPS::Rock => RPS::Paper,
                RPS::Paper => RPS::Scissors,
                RPS::Scissors => RPS::Rock,
            },
            _ => panic!("Couldn't convert player's move"),
        };

        games.push((opponent, player));
    }

    return score_games(games);
}
