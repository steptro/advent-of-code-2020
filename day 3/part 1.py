with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

count = 0
column = 0

for x in data:
    length = len(x)

    if x[column % length] == '#':
        count += 1

    column += 3

print(count)  # 257
