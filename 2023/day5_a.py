blocks = [lines.split("\n") for lines in open("data/5").read().split("\n\n")]
seeds  = [int(x) for x in blocks[0][0].split(" ")[1:]]
layers = [[(s, s + l, d - s) for d, s, l in [[int(x) for x in line.split()] for line in lines[1:] if line != ""]] for lines in blocks[1:]]

locations = []

for seed in seeds:
    current = seed
    for layer in layers:
        for start, stop, offset in layer:
            if start <= current < stop:
                current += offset
                break

    locations.append(current)

print(min(locations))
