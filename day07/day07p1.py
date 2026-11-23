from dataclasses import dataclass
from functools import cmp_to_key
from collections import Counter


card_rankings = list("AKQJT98765432")

@dataclass
class Hand:
    cards: str
    bet: int

    def get_hand_rank(self):
        counts = Counter(self.cards)
        if len(counts) == 1:
            return 1
        card_counts = sorted(list(counts.values()), reverse=True)
        if card_counts[0] == 4:
            return 2
        elif card_counts[0] == 3 and card_counts[1] == 2:
            return 3
        elif card_counts[0] == 3:
            return 4
        elif card_counts[0] == 2 and card_counts[1] == 2:
            return 5
        elif card_counts[0] == 2:
            return 6
        else:
            rank = 100000
            for c in self.cards:
                rank = min(rank, card_rankings.index(c) + 7)
            return rank
    
    def break_tie(self, other_hand) -> bool:
        for l, r in zip(self.cards, other_hand.cards):
            l_rank = card_rankings.index(l)
            r_rank = card_rankings.index(r)
            if l_rank > r_rank:
                return True
            elif l_rank < r_rank:
                return False
        assert False      
        

with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")

hands = []
for line in data:
    components = line.split(" ")
    hands.append(Hand(components[0], int(components[1])))
print(hands)

def s(a, b):
    a_rank = a.get_hand_rank()
    b_rank = b.get_hand_rank()
    if a_rank > b_rank:
        return -1
    elif a_rank == b_rank:
        if a.break_tie(b):
            return -1
        else:
            return 1
    else:
        return 1

hands.sort(key=cmp_to_key(s))
print(hands)

winnings = 0
for i, h in enumerate(hands):
    index = i + 1
    winnings += index * h.bet
print(winnings)