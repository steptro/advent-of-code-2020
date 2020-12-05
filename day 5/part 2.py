with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

taken_seats = []


def calculate_value(boarding_pass):
    r1 = 0
    r2 = 128

    row = boarding_pass[0:7]
    column = boarding_pass[7:10]

    for i in row:
        if i == 'F':
            r2 = r2 - (r2 - r1) / 2

        if i == 'B':
            r1 = r1 + (r2 - r1) / 2

    row = r2 - 1 if row[6] == 'F' else r1

    r3 = 0
    r4 = 8

    for j in column:
        if j == 'L':
            r4 = r4 - (r4 - r3) / 2

        if j == 'R':
            r3 = r3 + (r4 - r3) / 2

    column = r4 - 1 if column[2] == 'L' else r3

    return row * 8 + column


for x in data:
    taken_seats.append(calculate_value(x))

taken_seats.sort()

taken_seats = list(map(int, taken_seats))

counter = taken_seats[0]
for k in range(taken_seats[0], len(taken_seats)):
    if k not in taken_seats:
        break

    counter = counter + 1

print(counter)  # 659
