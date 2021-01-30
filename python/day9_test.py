import unittest
import day9


class Day9Test(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(
            127,
            day9.part1("../inputs/day9_example.txt", 5)
        )

    def test_part1(self):
        self.assertEqual(
            90433990,
            day9.part1("../inputs/day9.txt", 25)
        )

    def test_part2_example(self):
        self.assertEqual(
            62,
            day9.part2("../inputs/day9_example.txt", 127)
        )

    def test_part2(self):
        self.assertEqual(
            11691646,
            day9.part2("../inputs/day9.txt", 90433990)
        )


if __name__ == '__main__':
    unittest.main()
