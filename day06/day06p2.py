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


time = int(data[0].split(": ")[1].replace(" ", ""))
distance = int(data[1].split(": ")[1].replace(" ", ""))
race = Race(time, distance)
print(race)

win_count = 0
for i in range(1, race.time + 1):
    if race.can_win(i):
        win_count += 1
print(win_count)
