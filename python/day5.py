from collections import namedtuple

SeatPos = namedtuple('SeatPos', ['row', 'column'])


def seat_id(pos: SeatPos) -> int:
    return pos.row * 8 + pos.column


SeatRange = namedtuple('SeatRange', ['min', 'max'])

max_row = 128
max_col = 8

# binary space partition search
def find_seat_pos(seat_str):
    seat_row = binary_partition(seat_str,
                                SeatRange(0, max_row),
                                "F", "B")
    seat_col = binary_partition(seat_str,
                                SeatRange(0, max_col),
                                "L", "R")
    return SeatPos(seat_row, seat_col)


def binary_partition(seat_str, my_range, lower, upper):
    for c in seat_str:
        if c == lower:
            my_range = SeatRange(my_range.min, midpoint(my_range))
        elif c == upper:
            my_range = SeatRange(midpoint(my_range), my_range.max)
    return my_range.min


def midpoint(pos: SeatRange):
    return pos.min + round((pos.max - pos.min) / 2)


# finds the max id
def part1(filename):
    with open(filename) as seats_file:
        return max([
            seat_id(find_seat_pos(seat_str))
            for seat_str in seats_file.readlines()
        ])

def part2(filename):
    with open(filename) as seats_file:
        all_ids = [
            seat_id(find_seat_pos(seat_str))
            for seat_str in seats_file
        ]
        for i in all_ids:
            if not (i + 1) in all_ids and (i + 2) in all_ids:
                return i + 1