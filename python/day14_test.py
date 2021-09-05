import unittest

import day14


class Day14Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            165,
            day14.part1("""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""")
        )

    def test_part1(self):
        with open("../inputs/day14.txt") as day14_file:
            self.assertEqual(
                15018100062885,
                day14.part1(day14_file.read())
            )

    def test_part2_example(self):
        self.assertEqual(
            208,
            day14.part2("""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""")
        )

    def test_part2(self):
        with open("../inputs/day14.txt") as day14_file:
            self.assertEqual(
                5724245857696,
                day14.part2(day14_file.read())
            )


if __name__ == '__main__':
    unittest.main()
