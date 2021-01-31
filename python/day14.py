def apply_mask(num, mask):
    for i in range(0, len(mask)):
        if mask[-(i + 1)] == "1":
            num |= 1 << i
        elif mask[-(i + 1)] == "0":
            num &= ~(1 << i)
    return num


def add_to_unique_list(writes, addr, val):
    for i in range(0, len(writes)):
        if writes[i]['addr'] == addr:
            writes[i]['val'] = val
            return
    writes.append({'addr': addr, 'val': val})


def part1(data):
    mask = ""
    writes = []
    for line in data.splitlines():
        if "mask" in line:
            mask = line[7:]
        else:
            num = int(line.split("=")[1])
            num = apply_mask(num, mask)
            addr = int(line.split("[")[1].split("]")[0])
            add_to_unique_list(writes, addr, num)

    return sum([
        write['val']
        for write in writes
    ])


def apply_mask_part2(addr, mask):
    for i in range(0, len(mask)):
        if mask[-(i + 1)] == "1":
            addr |= 1 << i
        # elif mask[-(i + 1)] == "0":
        #     num &= ~(1 << i)
    all_nums = [addr]
    for i in range(0, len(mask)):
        if mask[-(i + 1)] == "X":
            new_nums = []
            for n in all_nums:
                new_nums.append(n | 1 << i)
                new_nums.append(n & ~(1 << i))
            all_nums = new_nums

    return all_nums


def part2(data):
    mask = ""
    writes = []
    for line in data.splitlines():
        if "mask" in line:
            mask = line[7:]
        else:
            num = int(line.split("=")[1])
            addr = int(line.split("[")[1].split("]")[0])
            all_addrs = apply_mask_part2(addr, mask)
            for a in all_addrs:
                add_to_unique_list(writes, a, num)

    return sum([
        write['val']
        for write in writes
    ])
