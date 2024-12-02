import heapq
from collections import defaultdict

data = [list(map(int, x)) for x in open("data/17").read().splitlines()]

opened = []
heapq.heappush(opened, (0, (0, 0), (0, 0), 0))

min_cost = defaultdict(lambda: 999999999999)

def get_neighbours(position: tuple[int, int]):
    neighbours = set()

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= position[0] + dx < len(data[0]) and \
           0 <= position[1] + dy < len(data):
            neighbours.add(((position[0] + dx, position[1] + dy), (dx, dy)))

    return neighbours

def search():
    while len(opened) > 0:
        current_cost, current_pos, current_delta, current_consecutive = heapq.heappop(opened)

        if current_pos[0] == len(data[0]) - 1 and current_pos[1] == len(data) - 1:
            return current_cost

        for next_pos, next_delta in get_neighbours(current_pos):
            if next_delta == (-current_delta[0], -current_delta[1]):
                continue

            next_cost = current_cost + data[next_pos[1]][next_pos[0]]

            next_consecutive = current_consecutive + 1 if current_delta == next_delta else 1

            if next_consecutive > 3 or next_cost >= min_cost[(next_pos, next_delta, next_consecutive)]:
                continue

            min_cost[(next_pos, next_delta, next_consecutive)] = next_cost

            heapq.heappush(opened, (next_cost, next_pos, next_delta, next_consecutive))

print(search())
