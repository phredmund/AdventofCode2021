class VentMap:
    def __init__(self):
        self.map = [[0] * 1000 for _ in range(1000)]

    def add_vent(self, coords, consider_diag):
        x1 = coords[0][0]
        y1 = coords[0][1]
        x2 = coords[1][0]
        y2 = coords[1][1]
        if x1 == x2:
            # X coordinates are the same
            for point in range(min(y1, y2), max(y1, y2) + 1):
                self.map[x1][point] += 1
        elif y1 == y2:
            # Y coordinates are the same
            for point in range(min(x1, x2), max(x1, x2) + 1):
                self.map[point][y1] += 1
        else:
            if not consider_diag:
                return
            # X and Y are both different
            diff = abs(x1 - x2)
            if x1 < x2 and y1 < y2:
                for point in range(diff + 1):
                    self.map[x1 + point][y1 + point] += 1
            elif x1 < x2 and y1 > y2:
                for point in range(diff + 1):
                    self.map[x1 + point][y1 - point] += 1
            elif x1 > x2 and y1 < y2:
                for point in range(diff + 1):
                    self.map[x1 - point][y1 + point] += 1
            elif x1 > x2 and y1 > y2:
                for point in range(diff + 1):
                    self.map[x1 - point][y1 - point] += 1
            else:
                print(f"We missed {coords}")

    def get_points(self):
        count = 0
        for row in self.map:
            for item in row:
                if item >= 2:
                    count += 1
        return count


def get_input():
    vents = []
    with open("input.txt", "r") as file:
        for line in file:
            vents.append(
                [list(map(int, line.strip().split(" -> ")[0].split(','))),
                 list(map(int, line.strip().split(" -> ")[1].split(',')))])
    return vents


def main():
    vents = get_input()
    map1 = VentMap()
    map2 = VentMap()
    for vent in vents:
        map1.add_vent(vent, False)
    print(f"Part 1: {map1.get_points()}")
    for vent in vents:
        map2.add_vent(vent, True)
    print(f"Part 2: {map2.get_points()}")

if __name__ == '__main__':
    main()
