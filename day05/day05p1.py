from dataclasses import dataclass
from typing import List, Optional

with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

@dataclass
class Mapping:
    destination_start: int
    source_start: int
    range_length: int

    def in_source_range(self, i: int) -> bool:
        return self.source_start <= i <= self.source_start + 1 + self.range_length
    
    def convert(self, i: int) -> Optional[int]:
        if not self.in_source_range(i):
            return None
        diff = self.destination_start - self.source_start
        return i + diff

def parse_maps(lines: str) -> List[Mapping]:
    lines = lines.split("\n")
    ranges = lines[1:]
    output = []
    for r in ranges:
        (d, s, r) = r.split(' ')
        output.append(Mapping(int(d), int(s), int(r)))
    return output

raw_mappings = data[1:]
steps: List[List[Mapping]] = list(map(parse_maps, raw_mappings))
seeds = list(map(int, data[0].split(": ")[1].split(" ")))
locations = []
for seed in seeds:
    current_value = seed
    for mappings in steps:
        for map in mappings:
            current_outcome = map.convert(current_value)
            if current_outcome:
                current_value = current_outcome
                break
        print(f'Seed {seed} has new value {current_value}')
    locations.append(current_value)
    print(f'Seed {seed} had final location {current_value}')
print(min(locations))