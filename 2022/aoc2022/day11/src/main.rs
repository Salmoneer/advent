use std::fs;
use std::collections::VecDeque;
use std::str::FromStr;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u64 {
    return monkey_business(20, 3);
}

fn part2() -> u64 {
    return monkey_business(10000, 1);
}

fn monkey_business(steps: u64, dividend: u64) -> u64 {
    let data = fs::read_to_string("input/day11.txt").expect("Couldn't read input file");
    let blocks = data.trim().split("\n\n");

    let mut monkeys: Vec<Monkey> = blocks
        .map(|block| block.parse())
        .collect::<Result<Vec<_>, _>>()
        .expect("Failed to parse monkeys");

    let global_modulus = monkeys.iter().map(|monkey| monkey.test_modulus).reduce(|a, b| a * b).expect("No monkeys");

    for _ in 0..steps {
        for i in 0..monkeys.len() {
            if monkeys[i].items.is_empty() { continue; }

            while let Some(item) = monkeys[i].items.pop_front() {
                monkeys[i].inspections += 1;

                let mut worry: u64 = item;
                worry = monkeys[i].operation.apply(worry);
                worry /= dividend;
                worry %= global_modulus;

                let target = if worry % monkeys[i].test_modulus == 0 {
                    monkeys[i].test_true
                } else {
                    monkeys[i].test_false
                };

                monkeys[target].items.push_back(worry);
            }
        }
    }

    let mut inspections = monkeys.iter().map(|monkey| monkey.inspections).collect::<Vec<_>>();
    inspections.sort_by(|a, b| b.cmp(a));
    return inspections[0] * inspections[1];
}

#[derive(Debug)]
struct MonkeyError;

enum Operand<T> {
    Number(T),
    Old,
}

impl<T: std::str::FromStr> FromStr for Operand<T> {
    type Err = MonkeyError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "old" => Ok(Operand::Old),
            n => Ok(Operand::Number(n.parse::<T>().map_err(|_| MonkeyError)?)),
        }
    }
}

enum Operation<T: std::ops::Add<Output = T> + std::ops::Mul<Output = T> + Copy> {
    Add(Operand<T>),
    Multiply(Operand<T>),
}

impl<T: std::ops::Add<Output = T> + std::ops::Mul<Output = T> + Copy> Operation<T> {
    pub fn apply(&self, old: T) -> T {
        let (Operation::Add(operand) | Operation::Multiply(operand)) = self;

        let operand = match operand {
            Operand::Number(n) => *n,
            Operand::Old => old,
        };

        return match self {
            Operation::Add(_) => old + operand,
            Operation::Multiply(_) => old * operand,
        }
    }
}

struct Monkey {
    items: VecDeque<u64>,
    operation: Operation<u64>,
    test_modulus: u64,
    test_true: usize,
    test_false: usize,
    inspections: u64,
}

impl FromStr for Monkey {
    type Err = MonkeyError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let lines: Vec<String> = s.split("\n").map(|x| x.to_string()).collect();

        let items_string: String = lines[1].chars().skip(18).collect();
        let items: VecDeque<u64> = items_string
            .split(", ")
            .map(|x| x.parse::<u64>().map_err(|_| MonkeyError))
            .collect::<Result<VecDeque<_>, _>>()?;

        let operator: char = lines[2]
            .chars()
            .nth(23)
            .map_or(Err(MonkeyError), |x| Ok(x))?;

        let operand_string: String = lines[2].chars().skip(25).collect::<String>();
        let operand: Operand<u64> = operand_string.parse()?;

        let operation = match operator {
            '+' => Operation::Add(operand),
            '*' => Operation::Multiply(operand),
            _ => return Err(MonkeyError),
        };

        let test_modulus = lines[3].chars().skip(21).collect::<String>().parse::<u64  >().map_err(|_| MonkeyError)?;
        let test_true    = lines[4].chars().skip(29).collect::<String>().parse::<usize>().map_err(|_| MonkeyError)?;
        let test_false   = lines[5].chars().skip(30).collect::<String>().parse::<usize>().map_err(|_| MonkeyError)?;

        return Ok(Monkey {
            items,
            operation,
            test_modulus,
            test_true,
            test_false,
            inspections: 0,
        });
    }
}
