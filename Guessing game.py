# This code implements a simple guessing game where the user has to guess a secret number within a limited number of chances. The program prompts the user to enter their guess, checks if it matches the secret number, and provides feedback accordingly. If the user guesses correctly, they win; if they exhaust their chances without guessing correctly, they lose.
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