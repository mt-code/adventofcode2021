horizontal = 0
depth = 0
aim = 0

with open('input.txt') as file:
    for line in file:
        command, value = line.split(' ', 1)

        if command == 'forward':
            horizontal += int(value)
            depth += (aim * int(value))
        elif command == 'up':
            aim -= int(value)
        elif command == 'down':
            aim += int(value)

print(horizontal * depth)
