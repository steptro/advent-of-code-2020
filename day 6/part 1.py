with open('input.txt', 'r') as f:
    data = list(f.read().split("\n\n"))

s = 0

for group in data:
    yes_answers = set()

    group = group.replace('\n', '')

    for answer in group:
        yes_answers.add(answer)

    s += len(yes_answers)

print(s)  # 6504
