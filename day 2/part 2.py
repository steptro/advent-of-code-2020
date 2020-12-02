import re

with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

count = 0

for x in data:
    split = list(filter(None, re.split('[- :]', x)))
    left = int(split[0])
    right = int(split[1])
    letter = split[2]
    password = split[3]

    letter1 = password[left - 1]
    letter2 = password[right - 1]

    if (letter1 == letter or letter2 == letter) and letter1 != letter2:
        count += 1

print(count)
