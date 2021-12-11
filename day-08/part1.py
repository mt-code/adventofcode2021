lines = open("input.txt").read().splitlines()
count = 0

for line in lines:
    signals, outputs = line.split(' | ', 1)

    for output in outputs.split(' '):
        if len(output) in [2, 3, 4, 7]:
            count += 1

print(f"The numbers 1, 4, 7 & 8 occur {count} times")
