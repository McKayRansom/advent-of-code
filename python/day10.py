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
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    # new idea: start from finished list and try and remove adapters
    combinations = [adapters]
    for comb in combinations:
        prev_diff = comb[1] - comb[0]
        prev_val = comb[1]
        for i in range(2, len(comb) - 1):
            # if we can remove the previous entry, do it
            val = comb[i]
            diff = val - prev_val
            if prev_diff + diff <= 3:
                new_comb = comb[i - 1:]
                new_comb[0] -= prev_diff
                combinations.append(new_comb)
            prev_diff = diff
            prev_val = val

    return len(combinations)
