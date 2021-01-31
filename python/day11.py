def get_neighbors_part1(seats, i, j):
    up = i - 1
    right = j + 1
    down = i + 1
    left = j - 1
    return (seats[up][right] == "#") + \
           (seats[i][right] == "#") + \
           (seats[down][j] == "#") + \
           (seats[down][right] == "#") + \
           (seats[down][left] == "#") + \
           (seats[i][left] == "#") + \
           (seats[up][left] == "#") + \
           (seats[up][j] == "#")


def inc_pos(seats, pos, direction):
    pos = (
        pos[0] + direction[0],
        pos[1] + direction[1]
    )
    if 0 < pos[0] < len(seats) and \
            0 < pos[1] < len(seats[0]):
        return pos
    else:
        return None


def seat_exists(seats, pos):
    s = seats[pos[0]][pos[1]]
    return s == "#" or s == "L"


def seat_occupied(seats, pos):
    return seats[pos[0]][pos[1]] == "#"


def has_neigh_dir(seats, pos, direction):
    while True:
        pos = inc_pos(seats, pos, direction)
        if not pos:
            return False
        elif seat_exists(seats, pos):
            return seat_occupied(seats, pos)


def get_neighbors_part2(seats, i, j):
    dirs = [
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
    ]
    neigh = 0
    for d in dirs:
        neigh += has_neigh_dir(seats, (i, j), d)

    return neigh


def simulate(seats_str, max_neigh, neigh_func):
    # insert extra seats to avoid bounds checking!
    seats = [
        "." + row + "."
        for row in seats_str.splitlines()
    ]
    extra_row = "." * len(seats[0])
    seats.insert(0, extra_row)
    seats.append(extra_row)

    output = ""
    for i in range(1, len(seats) - 1):
        for j in range(1, len(seats[0]) - 1):
            if seats[i][j] == ".":
                output += "."
            else:
                neigh = neigh_func(seats, i, j)
                if seats[i][j] == "L" and neigh == 0:
                    output += "#"
                elif seats[i][j] == "#" and neigh >= max_neigh:
                    output += "L"
                else:
                    output += seats[i][j]

        output += "\n"

    return output


def simulate_part1(seats_str):
    return simulate(seats_str, 4, get_neighbors_part1)


def simulate_part2(seats_str):
    return simulate(seats_str, 5, get_neighbors_part2)


def do_part(seats_str, simulate_func):
    prev_count = -1
    while True:
        seats_str = simulate_func(seats_str)
        count = seats_str.count("#")
        if count == prev_count:
            return count
        prev_count = count


def part1(seats_str: str):
    return do_part(seats_str, simulate_part1)


def part2(seats_str: str):
    return do_part(seats_str, simulate_part2)
