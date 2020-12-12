
def parse_map(file_name):
    tree_map = open(file_name, "r").readlines()
    return [str.strip(s) for s in tree_map]


# recursive version
def calc_trees_hit_recursive(tree_map, slope_x, slope_y, x=0, y=0):
    if y >= len(tree_map):
        return 0
    x = x % len(tree_map[0])
    tree_hit = tree_map[y][x] == "#"
    return tree_hit + calc_trees_hit_recursive(tree_map, slope_x, slope_y, x + slope_x, y + slope_y)


# iterative version
def calc_trees_hit(tree_map, slope_x, slope_y):
    trees_hit = 0
    x = 0
    for y in range(0, len(tree_map), slope_y):
        trees_hit += tree_map[y][x] == "#"
        x = (x + slope_x) % len(tree_map[0])
    return trees_hit


def calc_trees_hit_all_slopes(tree_map):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    result = 1
    for s in slopes:
        res = calc_trees_hit(tree_map, s[0], s[1])
        print("slope:", s[0], s[1], "result:", res)
        result *= res
    return result


print(calc_trees_hit(parse_map("day3_example.txt"), 3, 1))
print(calc_trees_hit_all_slopes(parse_map("day3_example.txt")))
# 2, 7, 3, 4, and 2

print(calc_trees_hit(parse_map("day3.txt"), 3, 1))
print(calc_trees_hit_all_slopes(parse_map("day3.txt")))
# 3064612320
