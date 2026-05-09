# This code removes duplicates from a list of numbers. It iterates through the original list and checks if each number is already in a new list (unum). If a number is not in the new list, it is added to it. Finally, the new list with unique numbers is printed.
num = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unum = []
for i in num:
    if i not in unum:
        unum.append(i)
print(unum)
