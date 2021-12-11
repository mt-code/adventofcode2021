positions = sorted(list(map(int, open("input.txt").readline().strip().split(','))))
value = positions[round(len(positions) / 2)]
fuel = 0

for pos in positions:
    while pos != value:
        fuel += 1
        pos += 1 if pos < value else -1

print(f"The least amount of fuel used to align all positions is: {fuel}")
