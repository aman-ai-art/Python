import random
counter = 0
number = random.randint(1, 100)
while counter < 10:
    guess = int(input("Guess the number between 1 and 100: "))
    counter += 1
    if guess == number:
        print("Congratulations! you guessed the number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
else:
    print(f"Sorry, you've used all your chances. The number was {number}.")
    
    