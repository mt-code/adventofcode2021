fishes = list(map(int, open("input.txt").readline().strip().split(',')))
days, fish_to_add = 80, 0

for day in range(0, days):
    for i in range(0, len(fishes)):
        if fishes[i] == 0:
            fish_to_add += 1
            fishes[i] = 6
        else:
            fishes[i] -= 1

    for i in range(0, fish_to_add):
        fishes.append(8)

    fish_to_add = 0

print(f"{len(fishes)} fish exist after {days} days")