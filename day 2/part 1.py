import re

with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

count = 0

for x in data:
    split = list(filter(None, re.split('[- :]', x)))
    minimum = int(split[0])
    maximum = int(split[1])
    letter = split[2]
    password = split[3]
    letterCount = password.count(letter)

    if minimum <= letterCount <= maximum:
        count += 1

print(count)