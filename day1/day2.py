
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


def password_valid(p):
    count = p["password"].count(p["letter"])
    return p["num1"] <= count <= p["num2"]


def calc_valid_passwords(passwords):
    return sum([
        password_valid(password)
        for password in passwords
    ])


info = parse_password_file("day2.txt")
print(calc_valid_passwords(info))
# Answers: 439, 584
