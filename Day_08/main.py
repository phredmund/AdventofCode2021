def get_input():
    with open("input.txt", "r") as file:
        return [[x.split() for x in line.split(" | ")] for line in file]


def main():
    readouts = get_input()
    count = 0
    for value in readouts:
        for output in value[1]:
            if len(output) in [2, 3, 4, 7]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
