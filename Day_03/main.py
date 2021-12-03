def get_input():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def add_pos(data, position):
    counter = 0
    for num in data:
        counter = counter + int(num[position])
    return counter


def assemble_readings(data):
    gamma = ""
    epsilon = ""
    for bit in range(len(data[0])):
        if add_pos(data, bit) >= len(data)/2:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    return gamma, epsilon


def get_rating(data, index=0, mode="oxy"):
    if len(data) == 1:
        return data[0]
    else:
        new_data = []
        most_common = (add_pos(data, index) >= len(data) / 2)
        if mode == "oxy":
            for num in data:
                if int(num[index]) == most_common:
                    new_data.append(num)
            return get_rating(new_data, index + 1, "oxy")
        elif mode == "co2":
            for num in data:
                if int(num[index]) != most_common:
                    new_data.append(num)
            return get_rating(new_data, index + 1, "co2")


def life_support(data):
    oxy_rating = int(get_rating(data, mode="oxy"), 2)
    print(f"Oxy rating: {oxy_rating}")
    co2_rating = int(get_rating(data, mode="co2"), 2)
    print(f"CO2 rating: {co2_rating}")
    return oxy_rating * co2_rating


def main():
    data = get_input()
    gam, ep = assemble_readings(data)
    print(f"Gamma: {gam}\nEpsilon: {ep}\n\tTotal: {int(gam, 2) * int(ep, 2)}")
    print(f"Life Support Rating: {life_support(data)}")


if __name__ == '__main__':
    main()
