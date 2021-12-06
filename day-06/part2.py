input = list(map(int, open("input.txt").readline().strip().split(',')))
fishes, days, fish_to_add = {}, 256, 0

for age in input:
    fishes[age] = fishes.get(age, 0) + 1

for day in range(0, days):
    new = {}

    for age in fishes.keys():
        if age == 0:
            new[6] = new.get(6, 0) + fishes[age]
            new[8] = new.get(8, 0) + fishes[age]
        else:
            new[age - 1] = new.get(age - 1, 0) + fishes[age]

    fishes = new

print(f"{sum(fishes.values())} fish exist after {days} days")