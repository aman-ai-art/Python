# This code demonstrates the use of if statements in Python to determine the weather conditions based on boolean variables. It checks if it's hot or cold and prints appropriate messages for each condition, as well as a default message for a lovely day.
is_hot = False
is_cold = False
if is_hot: 
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else: 
    print("It's a lovely day.")
print("Enjoy your day!")