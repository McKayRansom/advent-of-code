def parse_number_file():
    return [
        int(line)
        for line in
        open("day1.txt", "r").readlines()
    ]


def part1(nums):
    for n1 in nums:
        for n2 in nums:
            if n1 + n2 == 2020:
                print("Result:", n1 * n2)
                return


def part2(nums):
    for n1 in nums:
        for n2 in nums:
            for n3 in nums:
                if n1 + n2 + n3 == 2020:
                    print("Result:", n1 * n2 * n3)
                    return


numbers = parse_number_file()
part1(numbers)
part2(numbers)
# 800139
