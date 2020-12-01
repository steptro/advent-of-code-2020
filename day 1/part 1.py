class Found(Exception):
    pass


with open('input.txt', 'r') as f:
    data = list(map(int, f.read().split()))

data.sort()

try:
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            s = data[i] + data[j]

            if s == 2020:
                print(data[i] * data[j])
                raise Found
except Found:
    print("Found")
