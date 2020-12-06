with open('input.txt', 'r') as f:
    data = list(f.read().split("\n\n"))

s = 0

for group in data:
    people = group.split('\n')

    d = dict()

    for choices in people:
        for choice in choices:
            if choice not in d:
                d[choice] = 1
            else:
                d[choice] = d[choice] + 1

    for choice in d:
        if d[choice] == len(people):
            s += 1

print(s)  # 3351
