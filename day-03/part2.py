def match_bits(lines, index, match):
    count, values = 0, {"0": [], "1": []}

    for line in lines:
        values[line[index]].append(line)
        count += 1 if int(line[index]) > 0 else -1

    if count == 0:
        return values[match]

    return values["0"] if (count > 0 and match == "0") or (count < 0 and match == "1") else values["1"]


file = open("input.txt").read().splitlines()
oxygen_ratings, co2_ratings = file, file

i = 0
while len(oxygen_ratings) > 1:
    oxygen_ratings = match_bits(oxygen_ratings, i, "1")
    i += 1

i = 0
while len(co2_ratings) > 1:
    co2_ratings = match_bits(co2_ratings, i, "0")
    i += 1

print(int(oxygen_ratings[0], 2) * int(co2_ratings[0], 2))
