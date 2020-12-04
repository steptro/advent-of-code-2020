import string
import re

with open('input.txt', 'r') as f:
    data = list(f.read().split("\n\n"))


def check_birth_year(passport):
    if passport.find("byr") < 0:
        return False

    birthyear = passport[passport.find("byr"):].split(':')[1].split(" ")[0]
    birthyear = int(birthyear[0:4])

    if 1920 <= birthyear <= 2002:
        return True

    return False


def check_issue_year(passport):
    if "iyr" + ':' not in passport:
        return False

    issueyear = passport[passport.find("iyr"):].split(':')[1].split(" ")[0]
    issueyear = int(issueyear[0:4])

    if 2010 <= issueyear <= 2020:
        return True

    return False


def check_expiration_year(passport):
    if "eyr" + ':' not in passport:
        return False

    expirationyear = passport[passport.find("eyr"):].split(':')[1].split(" ")[0]
    expirationyear = int(expirationyear[0:4])

    if 2020 <= expirationyear <= 2030:
        return True

    return False


def check_height(passport):
    if "hgt" + ':' not in passport:
        return False

    height = passport[passport.find("hgt"):].split(':')[1]
    stripped = height.strip(string.ascii_letters + ' \n')

    if "in" in height and 59 <= int(stripped) <= 76:
        return True
    if "cm" in height and 150 <= int(stripped) <= 193:
        return True

    return False


def check_hair_color(passport):
    if "hcl" + ':' not in passport:
        return False

    color = passport[passport.find("hcl"):].split(':')[1]

    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color[0:7])


def check_eye_color(passport):
    if "ecl" + ':' not in passport:
        return False

    color = passport[passport.find("ecl"):].split(':')[1][0:3]
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if color in colors:
        return True

    return False


def check_passport_id(passport):
    if "pid" + ':' not in passport:
        return False

    p = passport[passport.find("pid"):].split(':')[1]

    return len(p.strip(string.ascii_letters + "\n ")) == 9


def is_valid(passport):
    if not check_birth_year(passport):
        return False

    if not check_issue_year(passport):
        return False

    if not check_expiration_year(passport):
        return False

    if not check_height(passport):
        return False

    if not check_hair_color(passport):
        return False

    if not check_eye_color(passport):
        return False

    if not check_passport_id(passport):
        return False

    return True


count = 0

for x in data:
    if is_valid(x):
        count += 1

print(count)  # 133

