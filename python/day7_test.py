import unittest
import day7

class Day7Tests(unittest.TestCase):
    def test_parse_bags(self):
        bags = day7.bags_parse("blue bags contain 1 red bag.")
        self.assertTrue(day7.bags_contain(bags, "blue", "red"))

    def test_bags_can_contain(self):
        bags = day7.bags_parse(
            "blue bags contain 1 red bag.\n"
            "red bags contain 1 blue bag.\n"
            "green bags contain no other bags.\n"
        )
        self.assertEqual(2,day7.bags_can_contain(bags, "red"))
        self.assertEqual(2,day7.bags_can_contain(bags, "blue"))

    def test_part1_example(self):
        with open("../inputs/day7_example.txt") as ex_file:
            bags = day7.bags_parse(ex_file.read())
            print(bags)
            self.assertTrue(day7.bags_contain(bags, "vibrant plum", "faded blue"))

            self.assertEqual(4, day7.bags_can_contain(bags, "shiny gold"))

    def test_part1(self):
        with open("../inputs/day7.txt") as day7_file:
            bags = day7.bags_parse(day7_file.read())
            self.assertEqual(261, day7.bags_can_contain(bags, "shiny gold"))

    def test_bags_count_contains(self):
        with open("../inputs/day7_example.txt") as ex_file:
            bags = day7.bags_parse(ex_file.read())
            self.assertEqual(32, day7.bags_count_contains(bags, "shiny gold"))

    def test_part2(self):
        with open("../inputs/day7.txt") as day7_file:
            bags = day7.bags_parse(day7_file.read())
            self.assertEqual(3765, day7.bags_count_contains(bags, "shiny gold"))

if __name__ == '__main__':
    unittest.main()
