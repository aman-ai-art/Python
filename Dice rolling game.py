import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
counter = 0
while True:
    choice = input("Roll the dice? (y/n): ")
    if choice.lower() == 'y':
        print(dice.roll())
        counter += 1
    elif choice.lower() == 'n':
        print(f"You rolled the dice {counter} times.")
        print("Thanks for playing the game!")
        break
    else: 
        print("Invalid choice.")
