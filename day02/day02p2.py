with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")

running_total = 0
for line in data:
    line_components = line.split(": ")
    (_, game_number) = line_components[0].split(" ")
    game_number = int(game_number)
    sets = line_components[1].split("; ")
    print(line)
    print(game_number)
    red = 0
    green = 0
    blue = 0
    for s in sets:
        cubes_seen = s.split(", ")
        for cs in cubes_seen:
            cube_count = int(cs.split(" ")[0])
            if cs.endswith("red"):
                red = max(red, cube_count)
            elif cs.endswith("green"):
                green = max(green, cube_count)
            elif cs.endswith("blue"):
                blue = max(blue, cube_count)
            else:
                assert False
    power = red * green * blue
    print(power)
    running_total += power
print(running_total)
