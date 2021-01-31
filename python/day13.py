import math


def parse_buses(csv_buses):
    return [
        int(bus)
        for bus in csv_buses.split(",")
        if bus != "x"
    ]


def find_next_bus(t, buses):
    diffs = [
        b - (t % b)
        for b in buses
    ]
    min_diff = 0
    for i in range(0, len(diffs)):
        if diffs[i] < diffs[min_diff]:
            min_diff = i

    return buses[min_diff], diffs[min_diff]


def part1(input_str):
    lines = input_str.splitlines()
    depart_time = int(lines[0])
    buses = parse_buses(lines[1])
    buses.sort()
    bus_no, wait_time = find_next_bus(depart_time, buses)
    return wait_time * bus_no


def parse_buses_in_order(csv_buses):
    return [
        int(bus) if bus != "x" else 0
        for bus in csv_buses.split(",")
    ]


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_list(nums: list):
    ans = 1
    for n in nums:
        ans = lcm(ans, n)
    return ans


def is_in_order_depart(t, buses):
    for b in buses:
        if b != 0 and t % b != 0:
            return False
        t += 1
    return True


# we know that the next answer is a multiple of the lcm from the previous answer
def find_in_order_departure(buses):
    if len(buses) == 1:
        return buses[0], buses[0]
    prev_ans, prev_lcm = find_in_order_departure(buses[:-1])
    if buses[-1] == 0:
        return prev_ans, prev_lcm
    t = prev_ans
    while True:
        t += prev_lcm
        if is_in_order_depart(t, buses):
            return t, lcm(prev_lcm, buses[-1])


def part2(input_str):
    buses = parse_buses_in_order(input_str.splitlines()[1])
    ans, _ = find_in_order_departure(buses)
    return ans
