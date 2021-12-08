def get_input():
    with open("input.txt", "r") as file:
        return list(map(int, file.readline().split(",")))


def fuel_calc(x):
    if x <= 1:
        return x
    else:
        total = x
        while x > 1:
            total += (x-1)
            x -= 1
        return total


def main():
    crabs = get_input()
    moves = []
    moves2 = []
    for position in range(max(crabs)):
        moves.append(sum(list(map(lambda x: abs(x - position), crabs))))
    print(f"Part 1: {min(moves)}")
    for position in range(max(crabs)):
        moves2.append(sum(list(map(lambda x: fuel_calc(abs(position - x)), crabs))))
    print(f"Part 2: {min(moves2)}")


if __name__ == '__main__':
    main()
