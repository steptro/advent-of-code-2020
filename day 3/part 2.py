with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))


def count_trees(right=3, down=1):
    count = 0
    column = 0
    row = 0

    for x in range(0, len(data), down):
        line = data[x]
        length = len(line)

        if line[column % length] == '#':
            count += 1

        column += right
        row += down

    return count


print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))  # 1744787392
