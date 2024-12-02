data = [list(x) for x in open("data/16").read().splitlines()]

class Beam:
    def __init__(self, px, py, vx, vy):
        self.pos_x = px
        self.pos_y = py
        self.vel_x = vx
        self.vel_y = vy

    def as_tuple(self):
        return (self.pos_x, self.pos_y, self.vel_x, self.vel_y)

def trace_beams(start_x, start_y, d_x, d_y):
    closed: set[tuple[int, int, int, int]] = set()
    closed.add((start_x, start_y, d_x, d_y))
    beams = [Beam(start_x, start_y, d_x, d_y)]

    while beams:
        for beam in beams:
            if data[beam.pos_y][beam.pos_x] == "\\":
                beam.vel_y, beam.vel_x = beam.vel_x, beam.vel_y

            elif data[beam.pos_y][beam.pos_x] == "/":
                beam.vel_y, beam.vel_x = -beam.vel_x, -beam.vel_y

            elif data[beam.pos_y][beam.pos_x] == "|" and beam.vel_x != 0:
                if (beam.pos_x, beam.pos_y, 0, 1) not in closed:
                    beams.append(Beam(beam.pos_x, beam.pos_y, 0, 1))
                if (beam.pos_x, beam.pos_y, 0, -1) not in closed:
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

    return len(set((x, y) for x, y, _, _ in closed))

maximum = 0

for dx in (-1, 1):
    for y in range(len(data)):
        maximum = max(trace_beams(0 if dx == 1 else len(data[0]) - 1, y, dx, 0), maximum)

for dy in (-1, 1):
    for x in range(len(data[0])):
        maximum = max(trace_beams(x, 0 if dy == 1 else len(data) - 1, 0, dy), maximum)

print(maximum)
