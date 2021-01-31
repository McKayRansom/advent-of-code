class Point:
    x = 0  # + east - west
    y = 0  # + north - south
    facing = 0  # degrees from east

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x \
               and self.y == other.y \
               and self.facing == other.facing

    def __repr__(self):
        return {
            'x': self.x,
            'y': self.y,
            'facing': self.facing
        }.__str__()

    def __str__(self):
        return "foo"

    def north(self, dst: int):
        self.y += dst

    def south(self, dst: int):
        self.y -= dst

    def east(self, dst: int):
        self.x += dst

    def west(self, dst: int):
        self.x -= dst

    def distance(self):
        return abs(self.x) + abs(self.y)

    def forward(self, value: int):
        if self.facing == 0:
            self.x += value
        elif self.facing == 90:
            self.y -= value
        elif self.facing == 180:
            self.x -= value
        elif self.facing == 270:
            self.y += value

    def left(self, value: int):
        self.facing -= value
        if self.facing < 0:
            self.facing += 360

    def right(self, value: int):
        self.facing += value
        if self.facing >= 360:
            self.facing -= 360

    def rotate_counterclockwise(self):
        dx = self.x
        dy = self.y
        self.x = -dy
        self.y = dx

    def rotate_left(self, degrees):
        for i in range(0, degrees, 90):
            self.rotate_counterclockwise()

    def rotate_right(self, degrees):
        for i in range(0, degrees, 90):
            self.rotate_clockwise()

    def rotate_clockwise(self):
        dx = self.x
        dy = self.y
        self.x = dy
        self.y = -dx

    def goto(self, waypoint, times):
        for i in range(0, times):
            self.x += waypoint.x
            self.y += waypoint.y


def find_distance_part1(directions: str):
    pos = Point()

    for cmd in directions.splitlines():
        action = cmd[0]
        value: int = int(cmd[1:])
        if action == "N":
            pos.north(value)
        elif action == "S":
            pos.south(value)
        elif action == "E":
            pos.east(value)
        elif action == "W":
            pos.west(value)
        elif action == "L":
            pos.left(value)
        elif action == "R":
            pos.right(value)
        elif action == "F":
            pos.forward(value)

    return pos.distance()


def find_distance_part2(directions):
    waypoint = Point(10, 1)
    ferry = Point()
    for cmd in directions.splitlines():
        action = cmd[0]
        value: int = int(cmd[1:])
        if action == "N":
            waypoint.north(value)
        elif action == "S":
            waypoint.south(value)
        elif action == "E":
            waypoint.east(value)
        elif action == "W":
            waypoint.west(value)
        elif action == "L":
            waypoint.rotate_left(value)
        elif action == "R":
            waypoint.rotate_right(value)
        elif action == "F":
            ferry.goto(waypoint, value)

    return ferry.distance()
