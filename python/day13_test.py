import unittest

import day13


class Day13Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            295,
            day13.part1("939\n7,13,x,x,59,x,31,19"),
        )

    def test_part1(self):
        with open("../inputs/day13.txt") as in_file:
            self.assertEqual(
                1835,
                day13.part1(in_file.read())
            )

    def test_part2_example(self):
        self.assertEqual(
            1068781,
            day13.part2("939\n7,13,x,x,59,x,31,19"),
        )

    def test_part2_long(self):
        self.assertEqual(
            1202161486,
            day13.part2("0\n1789,37,47,1889")
        )

    def test_part2_simple(self):
        self.assertEqual(
            77,
            day13.part2("0,\n7,13")
        )

    @unittest.skip("too long")
    def test_part2(self):
        with open("../inputs/day13.txt") as in_file:
            self.assertEqual(
                0,
                day13.part2(in_file.read())
            )


if __name__ == '__main__':
    unittest.main()
