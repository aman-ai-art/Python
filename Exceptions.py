# This code demonstrates how to handle multiple exceptions in Python using a single except block.
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello, {name}! You are {age} years old.")
except ValueError, TypeError, NameError, IndexError:
    print("Invalid input. Please enter a valid name and age.")