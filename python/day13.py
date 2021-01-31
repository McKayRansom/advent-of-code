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


def is_in_order_depart(t, buses):
    for b in buses:
        if b != 0 and t % b != 0:
            return False
        t += 1
    return True


def find_in_order_departure(buses):
    largest = buses.index(max(buses))
    t = buses[largest] - largest
    while True:
        t += buses[largest]
        if is_in_order_depart(t, buses):
            return t


def part2(input_str):
    buses = parse_buses_in_order(input_str.splitlines()[1])
    return find_in_order_departure(buses)
