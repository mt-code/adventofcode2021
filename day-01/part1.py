with open('input.txt') as file:
    count = 0
    previous = int(file.readline())

    for line in file:
        if int(line) > previous:
            count += 1

        previous = int(line)

    print(f"There are {count} increases in part 1")
