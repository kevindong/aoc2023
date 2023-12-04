with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")


def parse_numbers(s):
    parts = s.split(" ")
    return list(map(int, filter(lambda x: x != "", parts)))


def get_score(winning_numbers, selected_numbers):
    winning_numbers = set(winning_numbers)
    selected_numbers = set(selected_numbers)
    matches = len(winning_numbers.intersection(selected_numbers))
    if matches == 0:
        return 0
    return 2 ** (matches - 1)


total = 0
for card in data:
    (a, b) = card.split(" | ")
    (_, winning_numbers) = a.split(": ")
    winning_numbers = parse_numbers(winning_numbers)
    selected_numbers = parse_numbers(b)
    print(f"{winning_numbers}     {selected_numbers}")
    score = get_score(winning_numbers, selected_numbers)
    print(score)
    total += score
print(total)
