import string
from typing import Dict, Any


def parse_single_passport(passport_info):
    return Passport({
        info.split(":")[0]: info.split(":")[1]
        for info in passport_info.split(" ")
    })


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


class Passport:
    fields: Dict[Any, Any] = {}

    def __init__(self, fields):
        self.fields = fields

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

    def is_valid_part1(self):
        return self.required_items <= set(self.fields)

    def is_valid_part2(self):
        if not self.is_valid_part1():
            return False

        field_objects = [
            self.FieldByr(self.fields["byr"])
        ]
        return all([
            field.is_valid()
            for field in field_objects
        ])

    class FieldNumber:
        number = 0
        max_number = 0
        min_number = 0

        def __init__(self, int_string, min_number, max_number):
            self.number = int(int_string)
            self.min_number = min_number
            self.max_number = max_number

        def is_valid(self):
            return self.min_number <= self.number <= self.max_number

    class FieldByr(FieldNumber):
        max_byr = 2002
        min_byr = 1920

        def __init__(self, byr_string):
            super().__init__(byr_string, self.min_byr, self.max_byr)

    class FieldIyr(FieldNumber):
        max_iyr = 2020
        min_iyr = 2010

        def __init__(self, byr_string):
            super().__init__(byr_string, self.min_iyr, self.max_iyr)

    class FieldHgt(FieldNumber):
        max_hgt_cm = 193
        min_hgt_cm = 150
        max_hgt_in = 76
        min_hgt_in = 59

        def __init__(self, hgt_string):
            if "cm" in hgt_string:
                super().__init__(
                    hgt_string.replace("cm", ""),
                    self.min_hgt_cm,
                    self.max_hgt_cm
                )
            else:
                super().__init__(
                    hgt_string.replace("in", ""),
                    self.min_hgt_in,
                    self.max_hgt_in
                )

    # a # followed by exactly six characters 0-9 or a-f
    class FieldHcl:
        hcl_string = ""

        def __init__(self, hcl_string):
            self.hcl_string = hcl_string

        def is_valid(self):
            return len(self.hcl_string) == 7 \
                    and self.hcl_string[0] == "#" \
                    and all([
                        c in "abcdef" + string.digits
                        for c in self.hcl_string[1:]
                    ])

    class FieldEcl:
        eye_colors = [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]
        _ecl = ""
        def __init__(self, ecl_string):
            self._ecl = ecl_string

        def is_valid(self):
            return self._ecl in self.eye_colors


def part1():
    count = sum([
        passport.is_valid_part1()
        for passport in parse_passports("../inputs/day4.txt")
    ])
    print(count)


def part2():
    count = sum([
        passport.is_valid_part2()
        for passport in parse_passports("../inputs/day4.txt")
    ])
    print(count)


if __name__ == '__main__':
    # 208
    part1()
    part2()
