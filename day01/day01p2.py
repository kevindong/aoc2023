with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")

tokens = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for i in range(1, 10):
    tokens[str(i)] = i

total = 0
for line in data:
    left = (line[-1], len(line) - 1)
    for s, numerical_value in tokens.items():
        try:
            i = line.index(s)
            if i < left[1]:
                left = (str(numerical_value), i)
        except:
            continue
    right = (line[0], 0)
    for s, numerical_value in tokens.items():
        try:
            i = line.rindex(s)
            if i > right[1]:
                right = (str(numerical_value), i)
        except:
            continue
    num = int(left[0] + right[0])
    total += num
print(total)
