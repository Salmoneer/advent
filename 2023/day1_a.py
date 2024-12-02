import re

data = open("data/1").read()

s = 0

for line in data.splitlines():
    first_digit = re.search(r"\d", line).group(0)
    last_digit  = re.search(r"\d", line[::-1]).group(0)

    s += int(first_digit + last_digit)

print(s)
