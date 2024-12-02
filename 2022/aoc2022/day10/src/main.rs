use std::fs;
use std::collections::VecDeque;
use std::str::FromStr;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let mut cpu = parse_data();

    let mut s = 0;

    for i in 1.. {
        if !cpu.tick() {
            break;
        }

        if i % 40 == 20 {
            s += cpu.register * i;
        }
    }

    return s;
}

fn part2() -> String {
    let mut cpu = parse_data();

    let mut display = String::new();

    for _ in 0..6 {
        for x in 0..40 {
            if !cpu.tick() {
                panic!("Cpu ran out of instructions before finished drawing");
            }

            if (cpu.register - x).abs() <= 1 {
                display.push('#');
            } else {
                display.push('.');
            }
        }

        display.push('\n');
    }

    return display;
}

fn parse_data() -> Cpu {
    let data = fs::read_to_string("input/day10.txt").expect("Couldn't read file");
    let lines = data.trim().split("\n");

    let mut cpu = Cpu::new();

    for line in lines {
        cpu.instructions.push_back(line.parse().expect("Failed to parse instruction"));
    }

    return cpu;
}

#[derive(Debug)]
struct InstructionError;

#[derive(Debug)]
enum Instruction {
    Noop,
    Addx(i32),
}

impl FromStr for Instruction {
    type Err = InstructionError;

    fn from_str(string: &str) -> Result<Self, Self::Err> {
        if string == "noop" {
            return Ok(Instruction::Noop);
        } else if let Some((instruction, n)) = string.split_once(' ') {
            if instruction == "addx" {
                return n.parse::<i32>().map(Instruction::Addx).map_err(|_| InstructionError);
            } else {
                return Err(InstructionError);
            }
        } else {
            return Err(InstructionError);
        }
    }
}

#[derive(Debug)]
enum CpuAddState<T> {
    None,
    First(T),
    Second(T),
}

#[derive(Debug)]
struct Cpu {
    instructions: VecDeque<Instruction>,
    register: i32,
    state: CpuAddState<i32>,
}

impl Cpu {
    pub fn new() -> Cpu {
        Cpu {
            instructions: VecDeque::new(),
            register: 1,
            state: CpuAddState::None,
        }
    }

    pub fn tick(&mut self) -> bool {
        if let CpuAddState::First(x) = self.state {
            self.state = CpuAddState::Second(x);
        } else if let CpuAddState::Second(add) = self.state {
            self.register += add;
            self.state = CpuAddState::None;
        }

        if let CpuAddState::None = self.state {
            match self.instructions.pop_front() {
                Some(instruction) => {
                    if let Instruction::Addx(add) = instruction {
                        self.state = CpuAddState::First(add);
                    }
                },
                None => return false,
            }
        }

        return true;
    }
}
