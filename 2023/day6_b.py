import re

data = open("data/6").read().splitlines()

time, distance = [int(''.join(re.findall(r"\d+", y))) for y in data]

valid_times = 0

for t in range(time):
    if t * (time - t) > distance:
        valid_times += 1

print(valid_times)
