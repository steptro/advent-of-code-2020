with open('input.txt', 'r') as f:
    data = list(f.read().split("\n\n"))


def contains_fields(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in fields:
        if field + ':' not in passport:
            return False

    return True


count = 0

for x in data:
    if contains_fields(x):
        count += 1


print(count)


