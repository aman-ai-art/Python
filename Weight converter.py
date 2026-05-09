# This code is a simple weight converter that allows the user to convert their weight between kilograms (kg) and pounds (lb). The user is prompted to enter their weight and the unit they want to convert from. Based on the input, the code performs the appropriate conversion and displays the result. If the user enters an invalid unit, it prints an error message.
weight = float(input('Enter your weight: '))
unit = input('Enter K for kg or L for lb: ')
if unit.lower()=='l':
    weight_kg = weight * 0.4535
    print('your weight in kg is: ' + str(weight_kg))
elif unit.upper()=='K':
    weight_lb = weight / 0.4535
    print('your weight in lb is: ' + str(weight_lb))
else:
    print('Invalid unit.')
