# This code demonstrates different patterns of printing characters in Python. The first part prints a pattern of "X" characters in a specific format, while the second part prints "X" characters based on a list of numbers, where each number represents the count of "X" characters to be printed on a new line.
i = 1
num = 3
for i in range(num):
    print("XXXXXX")
    for j in range(i):
        print("XX")
print("\n")
i = [6, 2, 6, 2, 6]
for j in i:
    print("X" * j)