# This code demonstrates how to use dictionaries in Python to map digits to their corresponding word representations. The user is prompted to enter a number, and the program outputs the word for each digit in the number.
digits = {"1": "one", "2": "two", "3": "three" , "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
num = input("Enter a number: ")
for ch in num:
    if ch in digits:
        print(digits[ch], end=' ')
