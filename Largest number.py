# This code finds the largest number in a list of numbers. It iterates through the list and compares each number with the previous one to determine which is larger, ultimately printing the largest number found.
num = [5, 8, 9, 6, 10, 54, 23, 45, 67, 89]
i=0
for i in range(len(num)):
    if num[i-1] < num[i]:
        largest = num[i]
    else: 
        largest = num[i-1]
print("Largest number is: " + str(largest))
