import string


def parse_single_passport(passport_info):
    return {
        info.split(":")[0]: info.split(":")[1]
        for info in passport_info.split(" ")
    }


def parse_passports(file_name):
    with open(file_name, "r") as file:
        return [
            parse_single_passport(line)
            for line in file
                .read()
                .replace("\n\n", ",")
                .replace("\n", " ")
                .split(",")
        ]


def passport_is_valid_p1(fields):
    required_items = {
        "byr",  # (Birth Year)
        "iyr",  # (Issue Year)
        "eyr",  # (Expiration Year)
        "hgt",  # (Height)
        "hcl",  # (Hair Color)
        "ecl",  # (Eye Color)
        "pid",  # (Passport ID)
        # "cid",  # (Country ID) NOT REQUIRED
    }
    return required_items <= set(fields)


def passport_is_valid_p2(fields):
    if not passport_is_valid_p1(fields):
        return False

    return all([
        byr_is_valid(fields["byr"]),
        iyr_is_valid(fields["iyr"]),
        eyr_is_valid(fields["eyr"]),
        hgt_is_valid(fields["hgt"]),
        hcl_is_valid(fields["hcl"]),
        pid_is_valid(fields["pid"])
    ])

    # a # followed by exactly six characters 0-9 or a-f


def byr_is_valid(byr_string):
    min_byr = 1920
    max_byr = 2002
    return min_byr <= int(byr_string) <= max_byr


def iyr_is_valid(iyr_string):
    min_iyr = 2010
    max_iyr = 2020
    return min_iyr <= int(iyr_string) <= max_iyr


def eyr_is_valid(eyr_string):
    min_eyr = 2020
    max_eyr = 2030
    return min_eyr <= int(eyr_string) <= max_eyr


def hgt_is_valid(hgt_string):
    min_hgt_cm = 150
    max_hgt_cm = 193
    min_hgt_in = 59
    max_hgt_in = 76
    if "cm" in hgt_string:
        hgt = int(hgt_string.replace("cm", ""))
        return min_hgt_cm <= hgt <= max_hgt_cm
    elif "in" in hgt_string:
        hgt = int(hgt_string.replace("in", ""))
        return min_hgt_in <= hgt <= max_hgt_in
    else:
        return False


def hcl_is_valid(hcl_string):
    return len(hcl_string) == 7 \
           and hcl_string[0] == "#" \
           and all([
        c in "abcdef" + string.digits
        for c in hcl_string[1:]
    ])


def ecl_is_valid(ecl):
    eye_colors = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]
    for e in eye_colors:
        if e == ecl:
            return True


def pid_is_valid(pid_string):
    return len(pid_string) == 9 \
           and all([c in string.digits for c in pid_string])


def part1(filename):
    return sum([
        passport_is_valid_p1(passport)
        for passport in parse_passports(filename)
    ])


def part2(filename):
    return sum([
        passport_is_valid_p2(passport)
        for passport in parse_passports(filename)
    ])


if __name__ == '__main__':
    # 208
    print(part1("../inputs/day4.txt"))
    print(part2("../inputs/day4.txt"))
