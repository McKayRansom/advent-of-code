def parse_contains(contains):
    if contains == "no other bags":
        return (0, "")
    else:
        num = ""
        color = ""
        for c in contains:
            if c.isdigit():
                num += c
            else:
                color += c

        # remove trailing bags
        color = color.replace(" bags", "").replace(" bag", "")

        # remove leading space
        color = color[1:]

        return (
            int(num),
            color
        )

def split_colors(color_str):
    return [
        parse_contains(color)
        for color in color_str.split(", ")
    ]


def bag_split(my_bag):
    # print("\":" + my_bag + "\"")
    split = my_bag.split(" bags contain ")
    split[1] = split_colors(split[1])
    return split

def bags_parse(bags_str: str):
    return dict(bag_split(line[0:-1]) # remove . at end
                for line in bags_str.splitlines())


def bags_contain(bags, parent_color, child_color):
    return child_color in bags[parent_color][0][1]

# how many bags can contain color bag (with nesting)
def bags_can_contain(bags, color, blacklist=None):
    if blacklist is None:
        blacklist = []
    count = 0
    for key, value in bags.items():
        if key in blacklist:
            continue
        for contains in value:
            if color == contains[1]:
                # print("Found", color, "in", key)
                count += 1
                blacklist.append(key)
                count += bags_can_contain(bags, key, blacklist)
    return count


def bags_count_contains(bags, color):
    if color in bags:
        num = 0
        for contains in bags[color]:
            sub_num = bags_count_contains(bags, contains[1])
            num += contains[0] + contains[0] * sub_num
            # print(color, "contains", contains[0], "*", sub_num)
        # print("found", num, "in", color)
        return num
    else:
        return 0
