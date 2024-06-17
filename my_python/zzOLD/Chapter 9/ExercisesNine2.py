from random import randint

class Die():
    """ Make a Die, with a number of sides to roll """
    def __init__(self,sides=6):
        self.sides = sides
        self.rolls = []

    def roll(self,rolls):
        """Roll the dice"""
        i = 0
        while i < rolls:
            res = randint(1,self.sides)
            print("You rolled a: " + str(res))
            self.rolls.append(res)
            i += 1
        print()

    def saved_rolls(self,history):
        """see roll history"""
        for roll in self.rolls[-history:]:
            print("You previously rolled a: " + str(roll))
        print()

    def roll_stats(self):
        """ Find some basic statistics on your rolls"""
        
        mean = int(sum(self.rolls)/len(self.rolls))
        maximum = max(self.rolls)
        minimum = min(self.rolls)
        
        print("your mean roll was: " + str(mean))
        print("your maximum rolls was: " + str(maximum))
        print("your minimum roll was: " + str(minimum) + "\n")
