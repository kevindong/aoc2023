def read_inputs():
    with open("input.txt", "r") as f:
        raw_data = f.read()

    raw_data = raw_data.split("\n")
    data = []
    for line in raw_data:
        data.append([])
        for c in line:
            data[-1].append((c, None))
    return data


def expand(grid, i, j) -> int:
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
    num = 0
    for n in range(0, len(grid[i])):
        (current_c, is_included) = grid[i][n]
        if is_included:
            num *= 10
            num += int(current_c)
        grid[i][n] = (current_c, None)
    return num


offsets = set()
for i in range(-1, 2):
    for j in range(-1, 2):
        offsets.add((i, j))
offsets.remove((0, 0))
offsets = list(offsets)


def is_number(grid, i, j):
    if (not 0 <= i < len(grid)) or (not 0 <= j < len(grid[i])):
        return False
    return grid[i][j][0].isdigit()


def flip(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c = grid[i][j][0]
            if c != "*":
                continue
            candidate_numbers = []
            top_left_is_number = is_number(grid, i - 1, j - 1)
            top_above_is_number = is_number(grid, i - 1, j)
            top_right_is_number = is_number(grid, i - 1, j + 1)
            if not top_above_is_number:
                if top_left_is_number:
                    candidate_numbers.append((i - 1, j - 1))
                if top_right_is_number:
                    candidate_numbers.append((i - 1, j + 1))
            else:
                candidate_numbers.append((i - 1, j))
            if is_number(grid, i, j - 1):
                candidate_numbers.append((i, j - 1))
            if is_number(grid, i, j + 1):
                candidate_numbers.append((i, j + 1))
            bottom_left_is_number = is_number(grid, i + 1, j - 1)
            bottom_down_is_number = is_number(grid, i + 1, j)
            bottom_right_is_number = is_number(grid, i + 1, j + 1)
            if not bottom_down_is_number:
                if bottom_left_is_number:
                    candidate_numbers.append((i + 1, j - 1))
                if bottom_right_is_number:
                    candidate_numbers.append((i + 1, j + 1))
            else:
                candidate_numbers.append((i + 1, j))
            if len(candidate_numbers) != 2:
                continue
            first = expand(grid, candidate_numbers[0][0], candidate_numbers[0][1])
            second = expand(grid, candidate_numbers[1][0], candidate_numbers[1][1])
            total += first * second
    return total


grid = read_inputs()
print(flip(grid))
