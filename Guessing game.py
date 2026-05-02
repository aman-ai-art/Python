secret_number = 5
chances = 0
limit = 3
while chances < limit:
    guess = int(input('Guess the number: '))
    if guess == secret_number:
        print("Your won!")
        break
    elif chances == limit - 1:
        print("You lost! Try later.")
    else:
        print("Try again.")
    chances = chances + 1