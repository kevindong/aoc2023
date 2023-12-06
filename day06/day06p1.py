from dataclasses import dataclass

with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")


@dataclass
class Race:
    time: int
    distance: int

    def can_win(self, speed):
        time_left = self.time - speed
        distance_traveled = time_left * speed
        return distance_traveled > self.distance


times = list(map(int, filter(lambda x: x != "", data[0].split(": ")[1].split(" "))))
distances = list(map(int, filter(lambda x: x != "", data[1].split(": ")[1].split(" "))))
races = [Race(t, d) for t, d in zip(times, distances)]

ways_to_win = 1
for race in races:
    win_count = 0
    for i in range(1, race.time + 1):
        if race.can_win(i):
            win_count += 1
    ways_to_win *= win_count
print(ways_to_win)
