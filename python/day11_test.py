import unittest

import day11

test_seats = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


class Day11Test(unittest.TestCase):
    def test_simulate_empty(self):
        self.assertEqual(
            """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""",
            day11.simulate_part1(test_seats)
        )

    def test_simulate_1(self):
        result = day11.simulate_part1(
            day11.simulate_part1(test_seats)
        )
        self.assertEqual(
            """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""",
            result
        )

    def test_part1_example(self):
        self.assertEqual(
            37,
            day11.part1(test_seats)
        )

    def test_part1(self):
        with open("../inputs/day11.txt") as day11_file:
            self.assertEqual(
                2093,
                day11.part1(day11_file.read())
            )

    def test_part2_example(self):
        self.assertEqual(
            26,
            day11.part2(test_seats)
        )

    def test_part2(self):
        with open("../inputs/day11.txt") as day11_file:
            self.assertEqual(
                1862,
                day11.part2(day11_file.read())
            )


if __name__ == '__main__':
    unittest.main()
