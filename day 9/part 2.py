class Found(Exception):
    pass


with open('input.txt', 'r') as f:
    data = list(map(int, f.read().split("\n")))

current = 15690279
try:
    for k in range(0, len(data)):
        for j in range(k + 1, len(data)):
            lst = data[k:j]

            if sum(lst) == current:
                lst.sort()
                print(lst[0] + lst[len(lst) - 1])  # 2174232

                raise Found
except Found:
    print("Found")
