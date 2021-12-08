def get_input():
    with open("input.txt", "r") as file:
        return list(map(int, file.readline().split(",")))


def main():
    crabs = get_input()
    moves = []
    for position in range(max(crabs)):
        moves.append(sum(list(map(lambda x: abs(x - position), crabs))))
    print(f"Min moves: {min(moves)}")


if __name__ == '__main__':
    main()