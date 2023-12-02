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
    game_is_possible = True
    for s in sets:
        cubes_seen = s.split(", ")
        red = 0
        green = 0
        blue = 0
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
        set_is_possible = red <= 12 and green <= 13 and blue <= 14
        if not set_is_possible:
            game_is_possible = False
    if game_is_possible:
        running_total += game_number
print(running_total)
