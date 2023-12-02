with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")

total = 0
for line in data:
    num = None
    for c in line:
        if c.isdigit():
            num = c
            break
    for c in line[::-1]:
        if c.isdigit():
            num += c
            break
    total += int(num)
print(total)
