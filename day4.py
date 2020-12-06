import re

# cid is ignored and thus not added.
REQUIRED_FIELDS = ["byr",
                   "iyr",
                   "eyr",
                   "hgt",
                   "hcl",
                   "ecl",
                   "pid"]


def entry_to_dictionary(entry):
    return dict(pair.split(':') for pair in entry.replace('\n', ' ').split(' '))


def read_data_to_dictionary():
    with open('data/day4.txt') as f:
        data = f.read()
    passports = data.split('\n\n')
    return map(lambda passport: entry_to_dictionary(passport), passports)


def check_fields_validity(passport):
    pattern_height = re.compile(r"^(15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$")
    pattern_hair_color = re.compile(r"^#\w{6}$")
    eye_color_pattern = re.compile(r"amb|^b(lu|rn)|^gr(y|n)|hzl|oth")
    pid_pattern = re.compile(r"\d{9}$")
    if not (1920 <= int(passport['byr']) <= 2002 and
            2010 <= int(passport['iyr']) <= 2020 and
            2020 <= int(passport['eyr']) <= 2030):
        return False
    if not pattern_height.match(passport['hgt']):
        return False
    if not pattern_hair_color.match(passport['hcl']):
        return False
    if not eye_color_pattern.match(passport['ecl']):
        return False
    if not pid_pattern.match(passport['pid']):
        return False
    return True


def is_valid_passport(passport):
    passport.pop('cid', None)
    fields = passport.keys()
    if len(fields) != len(REQUIRED_FIELDS):
        return False
    if not check_fields_validity(passport):
        return False
    return True


def count_valid_passports():
    valid_passports = 0
    passports = read_data_to_dictionary()
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1
    return valid_passports


print(count_valid_passports())
