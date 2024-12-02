use std::fs;
use std::collections::HashSet;
use std::ops::{Add, AddAssign, Mul};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> usize {
    process_moves(2)
}

fn part2() -> usize {
    process_moves(10)
}

fn process_moves(length: usize) -> usize {
    let data = fs::read_to_string("input/day9.txt").expect("Unable to open input file");
    let lines: Vec<&str> = data.trim().split("\n").collect();
    let moves = lines_to_moves(lines);

    let mut bridge = Bridge::new(length);

    for mov in moves {
        bridge.move_head(mov);
    }

    return bridge.visited.len();
}

fn lines_to_moves(lines: Vec<&str>) -> Vec<Vec2> {
    let mut moves = Vec::new();

    for line in lines {
        for _ in 0..line.split_once(' ').expect("Failed to split line").1.parse::<u32>().expect("Failed to parse integer") {
            match line.chars().nth(0).expect("Get direction character failed") {
                'R' => moves.push(Vec2::new( 1,  0)),
                'L' => moves.push(Vec2::new(-1,  0)),
                'U' => moves.push(Vec2::new( 0,  1)),
                'D' => moves.push(Vec2::new( 0, -1)),
                _ => unreachable!(),
            }
        }
    }

    return moves;
}

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
struct Vec2 {
    x: i32,
    y: i32,
}

impl Vec2 {
    pub fn new(x: i32, y: i32) -> Vec2 {
        Vec2 { x, y }
    }
}

impl Add for Vec2 {
    type Output = Vec2;

    fn add(self, rhs: Self) -> Self::Output {
        return Vec2 {
            x: self.x + rhs.x,
            y: self.y + rhs.y
        };
    }
}

impl AddAssign for Vec2 {
    fn add_assign(&mut self, rhs: Self) {
        *self = *self + rhs;
    }
}

impl Mul for Vec2 {
    type Output = Vec2;

    fn mul(self, rhs: Self) -> Self::Output {
        return Vec2 {
            x: self.x * rhs.x,
            y: self.y * rhs.y,
        };
    }
}

struct Bridge {
    rope: Vec<Vec2>,
    visited: HashSet<Vec2>,
}

impl Bridge {
    pub fn new(length: usize) -> Bridge {
        assert!(length >= 2);

        Bridge {
            rope: vec![Vec2::new(0, 0); length],
            visited: HashSet::new(),
        }
    }

    pub fn move_head(&mut self, delta: Vec2) {
        self.rope[0] += delta;

        for i in 1..self.rope.len() {
            let dx = self.rope[i-1].x - self.rope[i].x;
            let dy = self.rope[i-1].y - self.rope[i].y;

            if dx.abs() > 1 || dy.abs() > 1 {
                if dx != 0 {
                    self.rope[i].x += dx / dx.abs();
                }
                if dy != 0 {
                    self.rope[i].y += dy / dy.abs();
                }
            }
        }

        self.visited.insert(self.rope[self.rope.len()-1]);
    }
}
