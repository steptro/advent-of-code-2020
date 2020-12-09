with open('input.txt', 'r') as f:
    data = list(map(int, f.read().split("\n")))

preamble = 25

for number in range(preamble, len(data)):
    current = data[number]
    previous = data[number - preamble:number]

    s = False

    for i in previous:
        for j in previous:
            if i != j and i + j == current:
                s = True

    if not s:
        print(current)  # 15690279
        break
