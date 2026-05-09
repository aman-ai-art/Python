# This code demonstrates various string methods in Python. It performs operations such as calculating the length of a string, converting it to uppercase and lowercase, capitalizing it, replacing a substring, and checking for the presence of a substring. Additionally, it calculates the length of a number by converting it to a string.
name = 'Aman Singh'
number = 123456789
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(len(str(number)))
name = name.replace('Singh', 'Kumar')
name = 'Mr. ' + name
name = name + ' Singh'
print(name)
print(name.find('Kumar'))
print('Aman' in name)