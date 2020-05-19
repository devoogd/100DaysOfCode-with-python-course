class Roll:
    def __init__(self, my_roll):
        self.my_roll = my_roll
        self.rolls = {'rock':'scissors', 'scissors': 'paper', 'paper': 'rock'}


    def can_defeat(self, their_roll):
        return self.rolls[self.my_roll] == their_roll

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

