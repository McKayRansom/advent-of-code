import string

def parse_part1(group_str: str):
    return set(group_str.replace("\n", ""))


def parse_groups(groups, group_func):
    return [
        group_func(g)
        for g in groups.split("\n\n")
    ]

def parse_part2(group_str):
    groups = set(string.ascii_lowercase)
    for line in group_str.splitlines():
        groups.intersection_update(set(line))
    return groups


def count_all(groups):
    return sum([
        len(g)
        for g in groups
    ])

def part1(filename):
    with open(filename) as day6_file:
        groups = parse_groups(day6_file.read(), parse_part1)
        return count_all(groups)

def part2(filename):
    with open(filename) as day6_file:
        groups = parse_groups(day6_file.read(), parse_part2)
        return count_all(groups)