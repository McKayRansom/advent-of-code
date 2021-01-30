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

    combinations = [[0]]
    for jolts_rating in adapters:
        new_combs = []
        for comb in combinations:
            max_jolts = comb[-1]
            if jolts_rating - max_jolts <= 3:
                new_combs.append(comb)
                new_combs.append(comb + [jolts_rating])
        combinations = new_combs

    # must get all the way to max jolts to adapt to device
    max_jolts = max(adapters)
    combinations = [
        comb
        for comb in combinations
        if comb[-1] == max_jolts
    ]

    return len(combinations)
