class BallPlayer:
    def __init__(self, nimi: str, number: int, goals: int, passes: int, minutes: int):
        self.nimi = nimi
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(nimi={self.nimi}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(ballers: list):
    holder = sorted(ballers, key=lambda blrs: blrs.goals)
    return holder[-1].nimi


def most_points(ballers: list):
    holder = sorted(ballers, key=lambda blrs: blrs.goals + blrs.passes)
    return (holder[-1].nimi, holder[-1].number)


def least_minutes(ballers: list):
    holder = sorted(ballers, key= lambda blrs: blrs.minutes)
    return holder[0]
