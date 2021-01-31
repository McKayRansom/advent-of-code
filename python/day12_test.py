import unittest

import day12


class Day12Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            25,
            day12.find_distance_part1("""F10
N3
F7
R90
F11""")
        )

    def test_part1(self):
        with open("../inputs/day12.txt") as day12_file:
            self.assertEqual(
                1482,
                day12.find_distance_part1(day12_file.read())
            )

    def test_point_rotate_left(self):
        pos = day12.Point(10, 0)
        pos.rotate_left(90)
        self.assertEqual(
            day12.Point(0, 10),
            pos
        )
        pos.rotate_left(90)
        self.assertEqual(
            day12.Point(-10, 0),
            pos
        )

    def test_point_rotate_right(self):
        pos = day12.Point(10, 0)
        pos.rotate_right(90)
        self.assertEqual(
            day12.Point(0, -10),
            pos
        )
        pos.rotate_right(90)
        self.assertEqual(
            day12.Point(-10, 0),
            pos
        )
        pos.rotate_right(180)
        self.assertEqual(
            day12.Point(10, 0),
            pos
        )

    # @unittest.skip("working on it")
    def test_part2_example(self):
        self.assertEqual(
            286,
            day12.find_distance_part2("""F10
N3
F7
R90
F11""")
        )

    def test_part2(self):
        with open("../inputs/day12.txt") as day12_file:
            self.assertEqual(
                48739,
                day12.find_distance_part2(day12_file.read())
            )


if __name__ == '__main__':
    unittest.main()
