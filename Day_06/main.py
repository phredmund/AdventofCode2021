def get_input():
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open("input.txt", "r") as file:
        for adult in list(map(int, file.readline().split(","))):
            fish[adult] += 1
    return fish


def advance(fishes, days):
    for day in range(days):
        newborns = fishes.pop(0)
        fishes[6] += newborns
        fishes.append(newborns)

def main():
    fishes = get_input()
    advance(fishes, 80)
    print(f"Part 1: {sum(fishes)}")
    advance(fishes, 256-80)
    print(f"Part 2: {sum(fishes)}")


if __name__ == '__main__':
    main()