
def parse_password_info(line):
    sections = line.split(" ")
    nums = sections[0].split("-")
    return {
        "num1": int(nums[0]),
        "num2": int(nums[1]),
        "letter": sections[1][0],
        "password": sections[2]
    }


def parse_password_file(file_name):
    lines = open(file_name, "r").readlines()
    return [parse_password_info(line) for line in lines]


def calc_valid_passwords(password_info):
    valid_passwords = 0
    for p in password_info:
        count = p["password"].count(p["letter"])
        if p["num1"] <= count <= p["num2"]:
            valid_passwords += 1

    return valid_passwords


info = parse_password_file("day2.txt")
print(calc_valid_passwords(info))

