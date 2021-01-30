import unittest
import day8

class Day8Test(unittest.TestCase):
    def setUp(self):
        day8.reset()

    def test_acc(self):
        day8.run_str("acc +7")
        self.assertEqual(7, day8.accumulator)

    def test_jmp(self):
        day8.run_str("jmp +2\nacc +2\nacc +2")
        self.assertEqual(2, day8.accumulator)

    def test_nop(self):
        day8.run_str("nop +100")
        self.assertEqual(0, day8.accumulator)

    def test_loop(self):
        self.assertFalse(day8.run_str("jmp +0"))

    def test_part1_exampe(self):
        with open("../inputs/day8_example.txt") as ex_file:
            day8.run_str(ex_file.read())
            self.assertEqual(5, day8.accumulator)

    def test_part1(self):
        with open("../inputs/day8.txt") as day8_file:
            day8.run_str(day8_file.read())
            self.assertEqual(1610, day8.accumulator)

    def test_part2_example(self):
        with open("../inputs/day8_example.txt") as ex_file:
            day8.find_valid_run(ex_file.read())
            self.assertEqual(8, day8.accumulator)

    def test_part2(self):
        with open("../inputs/day8.txt") as day8_file:
            day8.find_valid_run(day8_file.read())
            self.assertEqual(1703, day8.accumulator)


if __name__ == '__main__':
    unittest.main()
