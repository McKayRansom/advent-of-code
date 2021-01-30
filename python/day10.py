def parse_number_file(filename):
    with open(filename) as num_file:
        return [
            int(line)
            for line in num_file.readlines()
        ]


def part1(filename):
    adapters = parse_number_file(filename)
    adapters.sort()
    diffs = []
    jolts = 0
    for jolts_rating in adapters:
        diffs.append(jolts_rating - jolts)
        jolts = jolts_rating

    device_jolts = jolts + 3
    diffs.append(device_jolts - jolts)

    return diffs.count(1) * diffs.count(3)


def part2(filename):
    adapters = parse_number_file(filename)
    adapters.sort()
    adapters.append(max(adapters) + 3)
    adapters.insert(0, 0)

    # new new idea, iterate through once and keep track of recent adaptors
    connect = [0, 0, 1]
    prev_val = -1
    for joltage in adapters:
        diff = joltage - prev_val
        prev_val = joltage
        # if there is a diff of 1 we can make a chain with below 1, 2, 3
        if diff == 1:
            connect.insert(0, connect[0] + connect[1] + connect[2])

        # if there is a diff of 2 we can only make a chain with below 1, 2
        elif diff == 2:
            connect.insert(0, 0)  # empty space behind us
            connect.insert(0, connect[1] + connect[2])
        # if there is a diff of 3 we can only make a chain with below 2
        elif diff == 3:
            # two empty spaces behind us
            connect.insert(0, 0)
            connect.insert(0, 0)
            connect.insert(0, connect[2])
        else:
            raise Exception("Bad joltage", diff)

    return connect[0]
