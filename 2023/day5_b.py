blocks = [lines.split("\n") for lines in open("data/5").read().split("\n\n")]
seeds  = [int(x) for x in blocks[0][0].split(" ")[1:]]
layers = [[(s, s + l, d - s) for d, s, l in [[int(x) for x in line.split()] for line in lines[1:] if line != ""]] for lines in blocks[1:]]

def translate(seed_start, seed_stop, layer):
    if seed_stop <= seed_start:
        raise Exception("Invalid range (shit the bed)")

    for start, stop, offset in layer:
        if start <= seed_start < stop and start < seed_stop <= stop:
            return [[seed_start + offset, seed_stop + offset]]
        
        if seed_stop <= start or stop <= seed_start:
            continue

        out = []

        if seed_start < start:
            out += translate(seed_start, start, layer)

        out.append([max(start, seed_start) + offset, min(stop, seed_stop) + offset])

        if stop < seed_stop:
            out += translate(stop, seed_stop, layer)

        return out

    return [[seed_start, seed_stop]]


locations = []

for seed_start, seed_stop in [[a, a + b] for a, b in zip(seeds[::2], seeds[1::2])]:
    phase = [[seed_start, seed_stop]]
    for layer in layers:
        phase = [new_phase for start, stop in phase for new_phase in translate(start, stop, layer)]

    locations += phase

print(min(locations)[0])
