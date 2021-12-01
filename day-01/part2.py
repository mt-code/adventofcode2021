with open('input.txt') as file:
    count = 0
    previous = False
    lines = file.readlines()

    for i in range(len(lines) - 2):
        total = 0

        for k in range(i, i + 3):
            total += int(lines[k])

        if previous and total > previous:
            count += 1

        previous = total

    print(f"There are {count} increases in part 2")
