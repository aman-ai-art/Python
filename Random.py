# This is a sample Python script. It demonstrates the use of the random module to simulate rolling a pair of dice. The Dice class has a method called roll that generates two random integers between 1 and 6, representing the outcome of rolling two dice. The results are returned as a tuple, which is then printed to the console.
import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll())