import re

data = open("data/1").read()

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

s = 0

for line in data.splitlines():
    first_digit = re.search(r"\d", line)
    last_digit  = re.search(r"\d", line[::-1])

    first_word = re.search("(" + "|".join(digits)       + ")", line)
    last_word  = re.search("(" + "|".join(digits)[::-1] + ")", line[::-1])

    if first_digit == None or first_word and first_word.span()[0] < first_digit.span()[0]:
        first = digits.index(first_word.group()) + 1
    else:
        first = int(first_digit.group())

    if last_digit == None or last_word and last_word.span()[0] < last_digit.span()[0]:
        last = digits.index(last_word.group()[::-1]) + 1
    else:
        last = int(last_digit.group())
        
    print(line + '\n', int(str(first) + str(last)))

    s += int(str(first) + str(last))

print(s)
