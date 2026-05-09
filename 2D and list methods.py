# This code demonstrates how to work with 2D lists (matrices) and various list methods in Python.
mat = [[1,2,3],[4,5,6],[7,8,9]]
for row in mat:
    for col in row:
        print(col, end=' ')
    print()  # Print a newline after each row
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print(list1)
list2.append(11)
print(list2)
list1.reverse()
print(list1)
print(list2.count(6))
list1.insert(5, 99)
print(list1)