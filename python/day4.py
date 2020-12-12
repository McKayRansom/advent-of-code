
def parse_single_passport(passport_info):
    return {
        info.split(":")[0]: info.split(":")[1]
        for info in passport_info.split(" ")
    }


def parse_passports(file_name):
    return [
        parse_single_passport(line)
        for line in open(file_name, "r")
        .read()
        .replace("\n\n", ",")
        .replace("\n", " ")
        .split(",")
    ]


def passport_valid(passport):
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
    return required_items <= set(passport)


def part1():
    print(parse_passports("../inputs/day4_example.txt"))

    for passport in parse_passports("../inputs/day4_example.txt"):
        print(passport_valid(passport))

    count = sum([
        passport_valid(passport)
        for passport in parse_passports("../inputs/day4.txt")
    ])
    print(count)
    # 208


part1()
