counts = [0] * 12
gamma_rate = ""
epsilon_rate = ""

with open("input.txt") as file:
    for line in file:
        for char_index, char in enumerate(line.strip()):
            counts[char_index] += 1 if int(char) > 0 else -1

    for count in counts:
        gamma_rate += "1" if count > 0 else "0"
        epsilon_rate += "1" if count <= 0 else "0"

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
