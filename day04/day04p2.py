with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")


def parse_numbers(s):
    parts = s.split(" ")
    return list(map(int, filter(lambda x: x != "", parts)))


def get_matches(winning_numbers, selected_numbers):
    winning_numbers = set(winning_numbers)
    selected_numbers = set(selected_numbers)
    return len(winning_numbers.intersection(selected_numbers))


db = {i: 1 for i in range(1, len(data) + 1)}

for i, card in enumerate(data):
    card_number = i + 1
    (a, b) = card.split(" | ")
    (_, winning_numbers) = a.split(": ")
    winning_numbers = parse_numbers(winning_numbers)
    selected_numbers = parse_numbers(b)
    print(f"{winning_numbers}     {selected_numbers}")
    matches = get_matches(winning_numbers, selected_numbers)
    for j in range(card_number + 1, card_number + 1 + matches):
        db[j] += db[card_number]
print(sum(db.values()))
