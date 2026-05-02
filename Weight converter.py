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
