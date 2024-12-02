use std::fs;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::cmp::Reverse;
use std::str::FromStr;

fn main() {
    let data = fs::read_to_string("input/day12.txt").expect("Couldn't read input");
    let heightmap = data.parse::<Heightmap>().expect("Couldn't parse heightmap");

    println!("{}", search(&heightmap, true));
    println!("{}", search(&heightmap, false));
}

fn search(heightmap: &Heightmap, ascend: bool) -> u32 {
    let start = if ascend { heightmap.start } else { heightmap.end };

    let mut closed: HashSet<usize> = HashSet::new();
    let mut opened: BinaryHeap<(Reverse<u32>, usize)> = BinaryHeap::from([(Reverse(0), start)]);

    let mut costs: HashMap<usize, u32> = HashMap::from([(start, 0)]);

    while let Some((cost, pos)) = opened.pop() {
        if (ascend && pos == heightmap.end) || (!ascend && heightmap.elevations[pos] == 0) {
            return cost.0;
        }

        if closed.insert(pos) {
            let new_cost = cost.0 + 1;

            for new_pos in neighbors(heightmap, pos, ascend) {
                let is_better_path = match costs.get(&new_pos) {
                    Some(&existing_cost) => new_cost < existing_cost,
                        None => true,
                };

                if is_better_path {
                    opened.push((Reverse(new_cost), new_pos));
                    costs.insert(new_pos, new_cost);
                }
            }
        }
    }

    unreachable!("Couldn't get to end");
}

fn neighbors(heightmap: &Heightmap, pos: usize, ascend: bool) -> Vec<usize> {
    const DELTAS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

    let mut neighbors = Vec::new();

    for (dx, dy) in DELTAS {
        let new_x: i32 = (pos as i32) % (heightmap.width as i32) + dx;
        let new_y: i32 = (pos as i32) / (heightmap.width as i32) + dy;

        if 0 <= new_x && new_x < heightmap.width as i32 && 0 <= new_y && new_y < heightmap.height as i32 {
            let new_pos = (new_y as usize * heightmap.width) + new_x as usize;
            let slope = heightmap.elevations[new_pos] as i32 - heightmap.elevations[pos] as i32;
            if ascend && slope <= 1 || !ascend && slope >= -1 {
                neighbors.push(new_pos);
            }
        }
    }

    return neighbors;
}

#[derive(Debug)]
struct HeightmapError;

#[derive(Debug)]
struct Heightmap {
    width: usize,
    height: usize,
    elevations: Vec<u32>,
    start: usize,
    end: usize,
}

impl FromStr for Heightmap {
    type Err = HeightmapError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let height = s.lines().count();
        let width = s.lines().nth(0).unwrap().len();

        let data = s.replace("\n", "");

        let start = data.find('S').expect("No start found");
        let end = data.find('E').expect("No end in sight");

        let elevations = data
            .replace("S", "a")
            .replace("E", "z")
            .chars()
            .map(|c| (c as u8 - b'a') as u32)
            .collect::<Vec<_>>();

        Ok(Heightmap {
            width,
            height,
            elevations,
            start,
            end,
        })
    }
}
