# This code prompts the user to enter their name and checks the length of the name. It ensures that the name is at least 3 characters long and less than 50 characters long, providing appropriate feedback based on the length of the name entered by the user.
name = input('Enter your name: ')
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be less than 50 characters.")
else: 
    print("Name looks good!")