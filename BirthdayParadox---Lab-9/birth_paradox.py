import random

class BirthdayParadox:
    def __init__(self, repeat=1000):
        self.repeat = repeat

    def has_duplicate(self, birthdays):
        # If set length < list length, there are duplicates
        return len(birthdays) != len(set(birthdays))

    def run(self, n):
        match = 0
        for _ in range(self.repeat):
            birthdays = [random.randint(1, 365) for _ in range(n)]
            if self.has_duplicate(birthdays):
                match = match + 1
        probability = match / self.repeat
        return probability
