horizontal = 0
depth = 0

with open('input.txt') as file:
    for line in file:
        command, value = line.split(' ', 1)

        if command == 'forward':
            horizontal += int(value)
        elif command == 'up':
            depth -= int(value)
        elif command == 'down':
            depth += int(value)

print(horizontal * depth)
