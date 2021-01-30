def num_in_any_sum(n, nums):
    for n1 in nums:
        for n2 in nums:
            if (n1 + n2) == n:
                return True
    return False

def parse_number_file(filename):
    with open(filename) as part1_file:
        return [
            int(line)
            for line in part1_file.readlines()
        ]

# returns first number that is not the sum of 2 numbers
# up to nums_back number back
def part1(filename, nums_back):
    numbers = parse_number_file(filename)
    previous_numbers = numbers[0:nums_back]
    for num in numbers[nums_back:]:
        if not num_in_any_sum(num, previous_numbers):
            return num
        previous_numbers.pop(0)
        previous_numbers.append(num)
    return None


# find contiguous sum of numbers which add to invalid number
# from part1
def part2(filename, target_num):
    numbers = parse_number_file(filename)
    sums = []
    for n in numbers:
        for s in sums:
            s['sum'] += n
            s['list'].append(n)
            if s['sum'] == target_num:
                return max(s['list']) + min(s['list'])
            if s['sum'] > target_num:
                sums.remove(s)
        sums.append({'sum':n, 'list':[n]})
    return None

