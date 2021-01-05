import unittest
import day5

test_passes = [
    {"seat": "BFFFBBFRRR", "pos": day5.SeatPos(70, 7), "id": 567},
    {"seat": "FFFBBBFRRR", "pos": day5.SeatPos(14, 7), "id": 119},
    {"seat": "BBFFBBFRLL", "pos": day5.SeatPos(102, 4), "id": 820}
]


class TestDay5(unittest.TestCase):
    def test_seat_id(self):
        for test_p in test_passes:
            self.assertEqual(
                test_p["id"],
                day5.seat_id(test_p["pos"])
            )

    def test_find_seat(self):
        for t in test_passes:
            self.assertEqual(
                t["pos"],
                day5.find_seat_pos(t["seat"]),
                "For Seat" + str(t)
            )

    def test_part_1(self):
        self.assertEqual(
            915,
            day5.part1("../inputs/day5.txt")
        )

    def test_part_2(self):
        self.assertEqual(
            699,
            day5.part2("../inputs/day5.txt")
        )


if __name__ == "__main__":
    unittest.main()
