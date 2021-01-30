import unittest

import day10


class Day10Test(unittest.TestCase):
    def test_part1_example_small(self):
        self.assertEqual(
            7 * 5,
            day10.part1("../inputs/day10_example_small.txt")
        )

    def test_part1_example_large(self):
        self.assertEqual(
            22 * 10,
            day10.part1("../inputs/day10_example_large.txt")
        )

    def test_part1(self):
        self.assertEqual(
            1917,
            day10.part1("../inputs/day10.txt")
        )

    def test_part2_example_small(self):
        self.assertEqual(
            8,
            day10.part2("../inputs/day10_example_small.txt")
        )

    def test_part2_example_large(self):
        self.assertEqual(
            19208,
            day10.part2("../inputs/day10_example_large.txt")
        )

    # @unittest.skip("takes too long?")
    def test_part2(self):
        self.assertEqual(
            113387824750592,
            day10.part2("../inputs/day10.txt")
        )


if __name__ == '__main__':
    unittest.main()
