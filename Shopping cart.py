# This code calculates the total price of items in a shopping cart based on their individual prices and quantities. It prompts the user to enter the quantity for each item, multiplies the quantity by the corresponding item price, and sums up the total price to display the final bill.
item_price = [100, 200, 300]
Quantity = [0, 0, 0]
Quantity[0] = int(input('Enter quantity for item 1: '))
Quantity[1] = int(input('Enter quantity for item 2: '))
Quantity[2] = int(input('Enter quantity for item 3: '))
total_price = item_price[0] * Quantity[0] + item_price[1] * Quantity[1] + item_price[2] * Quantity[2]
print("Total bill: " + str(total_price))
