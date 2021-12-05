positions = {}
lines = open("input.txt").read().splitlines()


def set_pos(x, y):
    if x not in positions:
        positions[x] = {}

    if y not in positions[x]:
        positions[x][y] = 1
    else:
        positions[x][y] += 1


for line in lines:
    pipe_start, pipe_end = line.split(' -> ', 1)
    start_x, start_y = map(int, pipe_start.split(',', 1))
    end_x, end_y = map(int, pipe_end.split(',', 1))

    if start_x == end_x:
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            set_pos(start_x, y)
    elif start_y == end_y:
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            set_pos(x, start_y)
    else:
        x = start_x
        y = start_y if start_x < end_x else start_y

        while True:
            set_pos(x, y)

            if x == end_x:
                break

            x += 1 if start_x < end_x else -1
            y += 1 if start_y < end_y else -1


count = 0
for x in positions.keys():
    for y in positions[x]:
        if positions[x][y] >= 2:
            count += 1

print(f"Total number of positions that a pipe crosses (including diagonals): {count}")