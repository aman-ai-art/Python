# This code demonstrates the use of tuples in Python, including counting occurrences of a specific value and unpacking a tuple into individual variables. The first part counts how many times the number 3 appears in the tuple 'num', while the second part unpacks the coordinates from the 'coord' tuple into separate variables x, y, and z, which are then printed.
num = (1, 2, 3, 4, 5)
print(num.count(3))
print('\n')
coord = (1, 2, 3)
x, y, z = coord
print(x, y, z)
