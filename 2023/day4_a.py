import re, math

data = open("data/4").read()

def batch(data, length):
    out = []
    for i in range(math.ceil(len(data) // length)):
        out.append(data[i * length : (i + 1) * length])

    return out

s = 0

for card in data.splitlines():
    numbers = re.search(r"Card[\ ]+\d+:( .*)", card).group(1)
    good_numbers, present_numbers = [[int(y.lstrip()) for y in batch(x, 3)] for x in numbers.split(' |')]

    winning_numbers = len([x for x in good_numbers if x in present_numbers]) - 1

    if winning_numbers >= 0:
        s += 2 ** winning_numbers

print(s)
