def load_input():
    depths = []
    with open("./input.txt", "r") as file:
        for line in file:
            depths.append(int(line.strip()))
    return depths


def part1():
    data = load_input()
    counter = 0
    depth1 = data[0]
    for depth in data:
        if depth > depth1:
            counter = counter + 1
        depth1 = depth
    print(f"Part 1: {counter}")


def part2():
    data = load_input()
    counter = 0
    start = 1
    end = 4
    total1 = data[0] + data[1] + data[3]
    while end <= len(data):
        total = 0
        for num in data[start:end]:
            total = total + num
        if total > total1:
            counter = counter + 1
        total1 = total
        start = start + 1
        end = end + 1
    print(f"Part 2: {counter}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()

#________$$$$
#_______$$__$
#_______$___$$
#_______$___$$
#_______$$___$$
#________$____$$
#________$$____$$$
#_________$$_____$$
#_________$$______$$
#__________$_______$$
#____$$$$$$$________$$
#__$$$_______________$$$$$$
#_$$____$$$$____________$$$
#_$___$$$__$$$____________$$
#_$$________$$$____________$
#__$$____$$$$$$____________$
#__$$$$$$$____$$___________$
#__$$_______$$$$___________$
#___$$$$$$$$$__$$_________$$
#____$________$$$$_____$$$$
#____$$____$$$$$$____$$$$$$
#_____$$$$$$____$$__$$
#_______$_____$$$_$$$
#________$$$$$$$$$$
