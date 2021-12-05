lines = open("input.txt").read().splitlines()
positions = {}

for line in lines:
    pipe_start, pipe_end = line.split(' -> ', 1)
    start_x, start_y = map(int, pipe_start.split(',', 1))
    end_x, end_y = map(int, pipe_end.split(',', 1))

    if start_x == end_x:
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            if start_x not in positions:
                positions[start_x] = {}

            if y not in positions[start_x]:
                positions[start_x][y] = 1
            else:
                positions[start_x][y] += 1
    elif start_y == end_y:
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            if x not in positions:
                positions[x] = {}

            if start_y not in positions[x]:
                positions[x][start_y] = 1
            else:
                positions[x][start_y] += 1

count = 0
for x in positions.keys():
    for y in positions[x]:
        if positions[x][y] >= 2:
            count += 1

print(f"Total number of positions that a pipe crosses: {count}")