import unittest
import day6


class Day6Tests(unittest.TestCase):
    test_groups = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    day6_file = "../inputs/day6.txt"

    def test_one_group_parse(self):
        self.assertEqual({"a", "b", "c"},
                         day6.parse_part1("abc")
                         )
        self.assertEqual({"a", "b", "c", "x", "y", "z"},
                         day6.parse_part1("abc\nxyz")
                         )

    def test_all_groups_parse(self):
        groups = day6.parse_groups(self.test_groups, day6.parse_part1)
        self.assertEqual(
            [{"a", "b", "c"},
             {"a", "b", "c"},
             {"a", "b", "c"},
             {"a"},
             {"b"}],
            groups
        )

        self.assertEqual(
            11,
            day6.count_all(groups)
        )

    def test_part1(self):
        self.assertEqual(
            7120,
            day6.part1(self.day6_file)
        )

    def test_one_group_parse_p2(self):
        groups = day6.parse_groups(self.test_groups, day6.parse_part2)
        self.assertEqual(
            [{"a", "b", "c"},
             set(),
             {"a"},
             {"a"},
             {"b"}],
            groups
        )

        self.assertEqual(
            6,
            day6.count_all(groups)
        )

    def test_part2(self):
        self.assertEqual(3570,
                         day6.part2(self.day6_file)
                         )


if __name__ == '__main__':
    unittest.main()
