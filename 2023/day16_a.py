data = [list(x) for x in open("data/16").read().splitlines()]

closed: set[tuple[int, int, int, int]] = set()
closed.add((0, 0, 1, 0))

class Beam:
    def __init__(self, px, py, vx, vy):
        self.pos_x = px
        self.pos_y = py
        self.vel_x = vx
        self.vel_y = vy

    def as_tuple(self):
        return (self.pos_x, self.pos_y, self.vel_x, self.vel_y)

beams = [Beam(0, 0, 1, 0)]

while beams:
    for beam in beams:
        if data[beam.pos_y][beam.pos_x] == "\\":
            beam.vel_y, beam.vel_x = beam.vel_x, beam.vel_y

        elif data[beam.pos_y][beam.pos_x] == "/":
            beam.vel_y, beam.vel_x = -beam.vel_x, -beam.vel_y

        elif data[beam.pos_y][beam.pos_x] == "|" and beam.vel_x != 0:
            if (beam.pos_x, beam.pos_y, 0, 1) not in closed:
                beams.append(Beam(beam.pos_x, beam.pos_y, 0, 1))
            if (beam.pos_x, beam.pos_y, 0, -1):
                beams.append(Beam(beam.pos_x, beam.pos_y, 0, -1))

            beams.remove(beam)
            continue

        elif data[beam.pos_y][beam.pos_x] == "-" and beam.vel_y != 0:
            if (beam.pos_x, beam.pos_y, 1, 0) not in closed:
                beams.append(Beam(beam.pos_x, beam.pos_y, 1, 0))
            if (beam.pos_x, beam.pos_y, -1, 0) not in closed:
                beams.append(Beam(beam.pos_x, beam.pos_y, -1, 0))

            beams.remove(beam)
            continue


        beam.pos_x += beam.vel_x
        beam.pos_y += beam.vel_y

        if 0 <= beam.pos_x < len(data[0]) and 0 <= beam.pos_y < len(data) and beam.as_tuple() not in closed:
            closed.add(beam.as_tuple())
        else:
            beams.remove(beam)

occupied = sorted(list(set((x, y) for x, y, _, _ in closed)))

grid = [["." for _ in range(len(data[0]))] for _ in range(len(data))]

for cell in occupied:
    grid[cell[1]][cell[0]] = "#"

for line in grid:
    print("".join(line))

print(len(occupied))
