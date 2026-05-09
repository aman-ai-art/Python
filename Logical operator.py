# This code demonstrates the use of logical operators in Python to evaluate different weather conditions based on boolean variables. It checks if it's hot or cold and prints appropriate messages for each condition, as well as a default message for a lovely day.
is_hot = False
is_cold = False
if is_hot and not is_cold:
    print("It's a hot day.")
elif is_hot and is_cold:
    print("It's a lovely day.")
elif not is_hot and is_cold:
    print("It's a cold day.")
else:
    print("It's a normal day.")