def read_inputs():
    with open("input.txt", "r") as f:
        raw_data = f.read()

    raw_data = raw_data.split("\n")
    data = []
    for line in raw_data:
        data.append([])
        for c in line:
            is_period = c == "."
            is_digit = c.isdigit()
            is_symbol = not is_period and not is_digit
            data[-1].append((c, is_symbol))
    return data


def expand(grid, i, j):
    if (not 0 <= i < len(grid)) or (not 0 <= j < len(grid[i])):
        return
    elif grid[i][j][1] or not grid[i][j][0].isdigit():
        return
    grid[i][j] = (grid[i][j][0], True)
    for n in range(j, -1, -1):
        current_c = grid[i][n][0]
        if not current_c.isdigit():
            break
        grid[i][n] = (current_c, True)
    for n in range(j, len(grid[i])):
        current_c = grid[i][n][0]
        if not current_c.isdigit():
            break
        grid[i][n] = (current_c, True)


offsets = set()
for i in range(-1, 2):
    for j in range(-1, 2):
        offsets.add((i, j))
offsets.remove((0, 0))
offsets = list(offsets)


def flip(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c = grid[i][j][0]
            is_period = c == "."
            is_digit = c.isdigit()
            is_symbol = not is_period and not is_digit
            if not is_symbol:
                continue
            for (x, y) in offsets:
                expand(grid, i + x, j + y)


def count(grid):
    total = 0
    for i in range(len(grid)):
        num = 0
        for j in range(len(grid[i])):
            if grid[i][j][0].isdigit() and grid[i][j][1]:
                num *= 10
                num += int(grid[i][j][0])
            else:
                total += num
                num = 0
        if grid[i][-1][0].isdigit():
            total += num
    return total


grid = read_inputs()
flip(grid)

for row in grid:
    print(row)

print(count(grid))
