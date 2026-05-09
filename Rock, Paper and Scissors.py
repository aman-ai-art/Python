import random
options = ["r", "p", "s"]
while True:
    choice = input("Enter you choice (rock(r), paper(p), scissors(s)): ")
    computer = random.choice(options)
    if choice == computer:
        print(f"Computer chose: {computer}")
        print("It's a tie!. Try again.")
    elif(choice == "r" and computer == "s") or (choice == "p" and computer == "r") or (choice == "s" and computer == "p"):
        print(f"Computer chose: {computer}")
        print("You win!")
    elif(choice == "r" and computer == "p") or (choice == "p" and computer == "s") or (choice == "s" and computer == "r"):
        print(f"Computer chose: {computer}")
        print("You lose! Try again.")
    else:
        print("Invalid input.")
    topper = input("Do you want to play again? (y/n): ")

    if topper.lower() != "y":
        print("Thanks for playing the game!")
        break
    
