class Submarine1:

    def __init__(self):
        self.horiz_pos = 0
        self.depth = 0

    def move(self, direction, magnitude):
        """
        Moves the submarine in the specified direction and by the specified magnitude
        :param direction: String containing a direction to move
            Ex:     forward
                    down
                    up
        :param magnitude: Integer specifying how much to move
        :return: None
        """
        move = {
            "forward": self._forward,
            "down": self._down,
            "up": self._up,
        }

        if direction in move:
            move[direction](magnitude)
        else:
            raise Exception(f"Improper move direction: {direction}")

    def _forward(self, magnitude):
        self.horiz_pos = self.horiz_pos + magnitude

    def _down(self, magnitude):
        self.depth = self.depth + magnitude

    def _up(self, magnitude):
        self.depth = self.depth - magnitude


class Submarine2(Submarine1):

    def __init__(self):
        super().__init__()
        self.aim = 0

    def _forward(self, magnitude):
        self.horiz_pos = self.horiz_pos + magnitude
        self.depth = self.depth + (self.aim * magnitude)

    def _down(self, magnitude):
        self.aim = self.aim + magnitude

    def _up(self, magnitude):
        self.aim = self.aim - magnitude


def load_input():
    directions = []
    with open("./input.txt", "r") as file:
        for line in file:
            directions.append(
                line.strip().split()
            )
    return directions


def main():
    sub1 = Submarine1()
    directions = load_input()
    for direction in directions:
        sub1.move(direction[0], int(direction[1]))
    print(f"Part 1 product: {sub1.horiz_pos * sub1.depth}")

    sub2 = Submarine2()
    for direction in directions:
        sub2.move(direction[0], int(direction[1]))
    print(f"Part 2 product: {sub2.horiz_pos * sub2.depth}")


if __name__ == '__main__':
    main()
