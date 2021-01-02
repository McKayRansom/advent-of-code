import unittest
import day4


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
            self.assertFalse(day4.Passport(bad_passport).is_valid_part1())

        self.assertTrue(day4.Passport(self.test_passport).is_valid_part1())

    def test_field_number(self):
        self.assertFalse(
            day4.Passport.FieldNumber(0, 1, 2).is_valid()
        )
        self.assertFalse(
            day4.Passport.FieldNumber(3, 1, 2).is_valid()
        )
        self.assertTrue(
            day4.Passport.FieldNumber(1, 1, 2).is_valid()
        )
        self.assertTrue(
            day4.Passport.FieldNumber(2, 1, 2).is_valid()
        )

    def test_field_height(self):
        self.assertFalse(
            day4.Passport.FieldHgt("160in").is_valid()
        )
        self.assertTrue(
            day4.Passport.FieldHgt("160cm").is_valid()
        )
        self.assertTrue(
            day4.Passport.FieldHgt("60in").is_valid()
        )
        self.assertFalse(
            day4.Passport.FieldHgt("60cm").is_valid()
        )

    def test_field_hair_color(self):
        self.assertTrue(
            day4.Passport.FieldHcl("#123abc").is_valid()
        )
        self.assertFalse(
            day4.Passport.FieldHcl("#123abz").is_valid()
        )
        self.assertFalse(
            day4.Passport.FieldHcl("123abc").is_valid()
        )

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
            self.assertTrue(
                day4.Passport.FieldEcl(color).is_valid()
            )

    def test_passport_is_valid_part2(self):
        return
        for passport in day4.parse_passports("../inputs/day4_invalid_passports.txt"):
            self.assertFalse(passport.is_valid_part2(), "passport invalid" + str(passport.fields))


if __name__ == '__main__':
    unittest.main()
