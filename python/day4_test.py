import unittest
from day4 import *


class Day4Tests(unittest.TestCase):
    test_passport = {
        "byr": 100,
        "iyr": 100,
        "eyr": 100,
        "hgt": 100,
        "hcl": 100,
        "ecl": 100,
        "pid": 100
    }

    def test_passport_is_valid_part1(self):
        for key in self.test_passport:
            bad_passport = self.test_passport.copy()
            bad_passport.pop(key)
            self.assertFalse(passport_is_valid_p1(bad_passport))

        self.assertTrue(passport_is_valid_p1(self.test_passport))

    def test_birth_year(self):
        self.assertFalse(byr_is_valid(2003))
        self.assertTrue(byr_is_valid(2000))

    def test_issue_year(self):
        self.assertFalse(iyr_is_valid(2009))
        self.assertTrue(iyr_is_valid(2015))

    def test_expire_year(self):
        self.assertFalse(eyr_is_valid(2019))
        self.assertTrue(eyr_is_valid(2030))

    def test_field_height(self):
        self.assertFalse(hgt_is_valid("160in"))
        self.assertTrue(hgt_is_valid("160cm"))
        self.assertTrue(hgt_is_valid("60in"))
        self.assertFalse(hgt_is_valid("60cm"))
        self.assertFalse(hgt_is_valid("60"))

    def test_field_hair_color(self):
        self.assertTrue(hcl_is_valid("#123abc"))
        self.assertFalse(hcl_is_valid("#123abz"))
        self.assertFalse(hcl_is_valid("123abc"))

    def test_field_eye_color(self):
        eye_colors = [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]
        for color in eye_colors:
            self.assertTrue(ecl_is_valid(color))
        self.assertFalse(ecl_is_valid("foo"))

    def test_field_pid(self):
        # their test cases
        self.assertTrue(pid_is_valid("000000001"))
        self.assertFalse(pid_is_valid("0123456789"))
        # added test cases
        self.assertFalse(pid_is_valid("foobar123"))
        self.assertFalse(pid_is_valid("012345"))

    def test_passport_is_valid_part2(self):
        for passport in parse_passports("../inputs/day4_invalid_passports.txt"):
            self.assertFalse(passport_is_valid_p2(passport), "passport invalid" + str(passport))

    def test_part1_example(self):
        self.assertEqual(2, part1("../inputs/day4_example.txt"))

    def test_part1(self):
        self.assertEqual(208, part1("../inputs/day4.txt"))

    def test_part2_example(self):
        self.assertEqual(2, part2("../inputs/day4_example.txt"))

    def test_part2(self):
        self.assertEqual(222, part2("../inputs/day4.txt"))


if __name__ == '__main__':
    unittest.main()
