import math

positions = list(map(int, open("input.txt").readline().strip().split(',')))
average = math.floor(sum(positions) / len(positions))
fuel = 0

for pos in positions:
    count = 0

    while pos != average:
        fuel += 1 + count
        count += 1
        pos += 1 if pos < average else -1

print(f"The lowest amount of fuel is: {fuel}")
