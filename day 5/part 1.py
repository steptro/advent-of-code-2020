with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

taken_seats = []


def calculate_value(boarding_pass):
    b_row = ''
    b_column = ''

    for i in boarding_pass:
        if i == 'F':
            b_row += '0'
        elif i == 'B':
            b_row += '1'
        elif i == 'L':
            b_column += '0'
        elif i == 'R':
            b_column += '1'

    row = int(b_row, base=2)
    column = int(b_column, base=2)

    return row * 8 + column


for x in data:
    taken_seats.append(calculate_value(x))

taken_seats.sort()
print(taken_seats)
