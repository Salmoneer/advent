use std::fs;
use std::str::FromStr;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> usize {
    let data = fs::read_to_string("input/day8.txt").expect("Couldn't read file");
    let forest: Forest = data.parse().expect("Couldn't parse input data");

    return forest.count_visible();
}

fn part2() -> usize {
    let data = fs::read_to_string("input/day8.txt").expect("Couldn't read file");
    let forest: Forest = data.parse().expect("Couldn't parse input data");

    return forest.max_scenic_score();
}

struct Forest {
    grid: Vec<Vec<i32>>,
    width: usize,
    height: usize,
}

impl Forest {
    pub fn count_visible(&self) -> usize {
        let mut s = 0;

        for x in 0..self.width {
            for y in 0..self.height {
                if self.is_visible(x, y) {
                    s += 1;
                }
            }
        }

        return s;
    }

    fn is_visible(&self, index_x: usize, index_y: usize) -> bool {
        let value = self.grid[index_y][index_x];

        return *self.grid[index_y].get(0..index_x).expect("Unwrap .get").iter().max().unwrap_or(&-1) < value ||
            *self.grid[index_y].get(index_x+1..).expect("Unwrap .get").iter().max().unwrap_or(&-1) < value ||
            self.grid.get(0..index_y).expect("Unwrap .get").iter().map(|row| row[index_x]).max().unwrap_or(-1) < value ||
            self.grid.get(index_y+1..).expect("Unwrap .get").iter().map(|row| row[index_x]).max().unwrap_or(-1) < value;
    }

    fn scenic_score(&self, index_x: usize, index_y: usize) -> usize {
        let value = self.grid[index_y][index_x];

        if index_x == 0 || index_x == self.width  - 1 ||
           index_y == 0 || index_y == self.height - 1 {
            return 0;
        }

        let mut total = 1;

        for iter in [self.grid.get(0..index_y).expect("Unwrap .get").iter().map(|row| row[index_x]).rev().collect::<Vec<_>>(),
                     self.grid[index_y][0..index_x].iter().rev().copied().collect::<Vec<_>>(),
                     self.grid[index_y][index_x+1..].iter().copied().collect::<Vec<_>>(),
                     self.grid.get(index_y+1..).expect("Unwrap .get").iter().map(|row| row[index_x]).collect::<Vec<_>>()
        ] {
            let mut s = 0;
            for y in iter {
                s += 1;
                if y >= value {
                    break;
                }
            }
            total *= s;
        }

        return total;
    }

    pub fn max_scenic_score(&self) -> usize {
        (0..self.width).flat_map(|x| (0..self.height).map(move |y| self.scenic_score(x, y))).max().expect("No scenic scores")
    }
}

#[derive(Debug)]
struct ForestParseError;

impl FromStr for Forest {
    type Err = ForestParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let data = s.to_string();
        let lines = data.trim().split("\n");

        let grid: Vec<Vec<i32>> = lines
            .map(|line| line
                 .chars()
                 .map(|c| c
                      .to_digit(10)
                      .map(|d| d as i32)
                      .ok_or(ForestParseError))
                 .collect::<Result<Vec<i32>, ForestParseError>>())
            .collect::<Result<Vec<Vec<i32>>, ForestParseError>>()?;

        let width = grid.get(0).unwrap_or(&Vec::new()).len();
        let height = grid.len();

        return Ok(Forest {
            grid,
            width,
            height,
        });
    }
}
