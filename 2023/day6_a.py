import re

data = open("data/6").read().splitlines()

time, distance = [[int(x) for x in re.findall(r"\d+", y)] for y in data]

p = 1

for race in range(len(time)):
    valid_times = 0

    for t in range(time[race]):
        if t * (time[race] - t) > distance[race]:
            valid_times += 1

    p *= valid_times

print(p)
