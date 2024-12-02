use std::fs;
use std::path::PathBuf;
use std::collections::HashMap;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> usize {
    let data = fs::read_to_string("input/day7.txt").expect("Error opening input file");
    let lines: Vec<&str> = data.split_terminator("\n").collect();

    let filesys = build_fs(&lines);

    return filesys.iter()
    .map(|x| x.total_size())
    .filter(|&size| size <= 100000)
    .sum();
}

fn part2() -> usize {
    let data = fs::read_to_string("input/day7.txt").expect("Error opening input file");
    let lines: Vec<&str> = data.split_terminator("\n").collect();

    let filesys = build_fs(&lines);

    let needed_space = 30000000 - (70000000 - filesys.total_size());

    return filesys.iter()
    .map(|x| x.total_size())
    .filter(|&size| size >= needed_space)
    .min()
    .unwrap();
}

fn build_fs<'a>(lines: &'a Vec<&str>) -> FsObject {
    let mut pwd: PathBuf = PathBuf::new();

    let mut filesys: FsObject = FsObject::Dir(HashMap::new());

    for line in lines.iter().skip(1) {
        if let Some(command) = line.strip_prefix("$ ") {
            if let Some(operand) = command.strip_prefix("cd ") {
                if operand == ".." {
                    pwd.pop();
                } else {
                    pwd.push(operand);
                }
            }
        } else {
            if let Some(dir_name) = line.strip_prefix("dir ") {
                if let FsObject::Dir(map) = filesys.get_path(&pwd) {
                    map.insert(dir_name.to_string(), FsObject::Dir(HashMap::new()));
                } else {
                    panic!("PWD is a file");
                }
            } else {
                let components: Vec<&str> = line.split(" ").collect();
                let size: usize = components[0].parse::<usize>().expect("Error parsing file size");
                let file_name: &str = components[1];

                if let FsObject::Dir(map) = filesys.get_path(&pwd) {
                    map.insert(file_name.to_string(), FsObject::File(size));
                } else {
                    panic!("PWD is a file");
                }
            }
        }
    }

    return filesys;
}

enum FsObject {
    File(usize),
    Dir(HashMap<String, FsObject>)
}

impl FsObject {
    fn get_child(&mut self, child: &str) -> &mut FsObject {
        match self {
            FsObject::Dir(map) => map.get_mut(child).expect("Error getting mutable child of dir map"),
            FsObject::File(_) => panic!("Cannot get child of file")
        }
    }

    pub fn get_path(&mut self, path: &PathBuf) -> &mut FsObject {
        let mut target = self;

        for component in path.components() {
            target = target.get_child(component.as_os_str().to_str().expect("Error converting pathbuf component to string"));
        }

        return target;
    }

    pub fn total_size(&self) -> usize {
        match self {
            FsObject::File(size) => *size,
            FsObject::Dir(map) => map.values().map(|x| x.total_size()).sum()
        }
    }

    pub fn iter<'a>(&'a self) -> FsIterator<'a> {
        return FsIterator::new(self);
    }
}

struct FsIterator<'a> {
    root: Option<&'a FsObject>,
    stack: Vec<&'a FsObject>,
}

impl<'a> FsIterator<'a> {
    pub fn new(root: &'a FsObject) -> FsIterator<'a> {
        return FsIterator {
            root: Some(root),
            stack: Vec::new(),
        };
    }
}

impl<'a> Iterator for FsIterator<'a> {
    type Item = &'a FsObject;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(root) = self.root {
            self.root = None;
            self.stack.push(root);
        }

        while let Some(element) = self.stack.pop() {
            if let FsObject::Dir(dir) = element {
                self.stack.append(&mut dir.values().collect::<Vec<_>>().clone());
                return Some(element);
            }
        }

        return None;
    }
}
